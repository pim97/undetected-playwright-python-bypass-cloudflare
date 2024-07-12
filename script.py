import asyncio
from playwright.async_api import async_playwright
from lib.scrappey import get_cookies_and_user_agent
import os
from dotenv import load_dotenv

load_dotenv()

# Get your API key on Scrappey.com
# We created a env_example_file, rename it to .env with the correct details
API_KEY = os.getenv('API_KEY')
PROXY_URL = os.getenv('PROXY_URL')
TARGET_URL = os.getenv('TARGET_URL')

# Chrome V126 example
async def chromev126():
    
    async with async_playwright() as p:
        # Get cookies and user agent from Scrappey
        cookie_object, user_agent, proxy_obj = get_cookies_and_user_agent(API_KEY, TARGET_URL, PROXY_URL, version=126, browser_name='chrome')

        for browser_type in [p.chromium]:
            browser = await browser_type.launch(headless=False, proxy=proxy_obj, channel='chrome')
            context = await browser.new_context(user_agent=user_agent)
            page = await context.new_page()
            
            await context.add_cookies(cookie_object)
            await page.goto(TARGET_URL)
            await page.wait_for_load_state('networkidle')
            await page.screenshot(path='screenshot_chrome.png')
            await browser.close()

# Firefox V126 example
async def firefox126():
    
    async with async_playwright() as p:
        # Get cookies and user agent from Scrappey
        cookie_object, user_agent, proxy_obj = get_cookies_and_user_agent(API_KEY, TARGET_URL, PROXY_URL, version=126, browser_name='firefox')

        for browser_type in [p.firefox]:
            browser = await browser_type.launch(headless=False, proxy=proxy_obj)
            context = await browser.new_context(user_agent=user_agent)
            page = await context.new_page()
            
            await context.add_cookies(cookie_object)
            await page.goto(TARGET_URL)
            await page.wait_for_load_state('networkidle')
            await page.screenshot(path='screenshot_firefox.png')
            await browser.close()

asyncio.run(firefox126())
asyncio.run(chromev126())
