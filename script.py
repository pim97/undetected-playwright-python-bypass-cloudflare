import asyncio
from playwright.async_api import async_playwright
from scrappey import get_proxy_object, get_cookies_and_user_agent, parse_cookie_string

# Configuration
# Get your API key on Scrappey.com
API_KEY = "API_KEY_HERE"
TARGET_URL = "https://topminecraftservers.org/vote/32492"
PROXY_URL = 'http://user:pass@host:ip'

# Get cookies and user agent from Scrappey
cookie_string, user_agent = get_cookies_and_user_agent(API_KEY, TARGET_URL, PROXY_URL)
cookies = parse_cookie_string(cookie_string, target_url=TARGET_URL)
proxyObj = get_proxy_object(PROXY_URL)

async def main():
    async with async_playwright() as p:
        for browser_type in [p.chromium]:
            browser = await browser_type.launch(headless=False, proxy=proxyObj, channel='chrome')
            context = await browser.new_context(user_agent=user_agent)
            page = await context.new_page()
            
            await context.add_cookies(cookies)
            await page.goto(TARGET_URL)
            await page.wait_for_load_state('networkidle')
            await page.screenshot(path='screenshot.png')
            await browser.close()

asyncio.run(main())
