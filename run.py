import requests
import asyncio
from playwright.async_api import async_playwright
from urllib.parse import urlparse

# Step 1: Send POST request and extract cookie and user agent
# Get your API key here: https://scrappey.com
url = "http://localhost:87/v1?key=YOUR_API_KEY_HERE"

proxy_url = 'http://user:pass@host:ip'
# Parse the proxy URL
parsed_url = urlparse(proxy_url)

# Extract the components
username = parsed_url.username
password = parsed_url.password
server = f"{parsed_url.scheme}://{parsed_url.hostname}:{parsed_url.port}"

# Create the proxy object
proxyObj = {
    "server": server,
    "username": username,
    "password": password
}

print(proxyObj)
headers = {
    "Content-Type": "application/json"
}
body = {
    "cmd": "request.get",
    "url": "https://www.arena-top100.com/index.php?a=in&u=sergey1234",
    "proxy": proxy_url,
    "noDriver": True,
    "browser": [
        {
            "name": "chrome",
            "minVersion": 126,
            "maxVersion": 126
        }
    ]
}

response = requests.post(url, json=body, headers=headers)
response_data = response.json()

cookie_string = response_data['solution']['cookieString']  # Adjust this according to the actual response structure
user_agent = response_data['solution']['userAgent']  # Adjust this according to the actual response structure

# Step 2: Extract domain from URL
target_url = 'https://www.arena-top100.com/index.php?a=in&u=sergey1234'
parsed_url = urlparse(target_url)
domain = parsed_url.netloc

def parse_cookie_string(cookie_string):
    cookies = []
    for cookie in cookie_string.split('; '):
        name, value = cookie.split('=', 1)
        cookies.append({
            'name': name,
            'value': value,
            'domain': domain,
            'path': '/'
        })
    return cookies

# Step 2: Use Playwright to launch a browser, set cookie and user agent, and navigate to a page
async def main():
    async with async_playwright() as p:
        for browser_type in [p.chromium]:
            browser = await browser_type.launch(headless=False, proxy=proxyObj)
            # page = await browser.new_page()
            context = await browser.new_context(user_agent=user_agent)
            page = await context.new_page()
            
            print(f"Setting cookie for domain {cookie_string}")
            print(f"Setting user agent {user_agent}")
            print(f"Domain to {domain}")
            
            cookies = parse_cookie_string(cookie_string)
            for cookie in cookies:
                print(f"Setting cookie: {cookie}")
            
            # Set the cookies
            await context.add_cookies(cookies)
            
            ua = await page.evaluate("() => navigator.userAgent")

            # Print the user agent
            print(f"User Agent: {ua}")
               
            await page.goto('https://www.arena-top100.com/index.php?a=in&u=sergey1234')
            await page.wait_for_load_state('networkidle')

            await browser.close()

asyncio.run(main())
