import asyncio
from playwright.async_api import async_playwright
from lib.scrappey import get_proxy_object, get_cookies_and_user_agent, parse_cookie_string
import os
from dotenv import load_dotenv

load_dotenv()

# Configuration set in .env file
# Get your API key on Scrappey.com, create an .env file and set the API_KEY and PROXY_URL
API_KEY = os.getenv('API_KEY')
PROXY_URL = os.getenv('PROXY_URL')
TARGET_URL = os.getenv('TARGET_URL')

# Get cookies and user agent from Scrappey
cookie_string, user_agent = get_cookies_and_user_agent(API_KEY, TARGET_URL, PROXY_URL)
cookies = parse_cookie_string(cookie_string, target_url=TARGET_URL)
proxyObj = get_proxy_object(PROXY_URL)

async def main():
    
    # Chrome example V126
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
