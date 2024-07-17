# Undetected Playwright Python CF Solver

This repository contains a Python script that sends a POST request to an API, extracts the cookie and user agent, and uses Playwright to set these cookies and user agent in a browser session while navigating to a specified URL through a proxy.

## Prerequisites

- Python 3.7+
- [Playwright](https://playwright.dev/python/docs/intro) for Python
- Required Python packages (listed in `requirements.txt`)

## Code example
```python
async with async_playwright() as p:
    cookie_object, user_agent, proxy_obj = get_cookies_and_user_agent(API_KEY, TARGET_URL, 
        PROXY_URL, version=126, browser_name='chrome')

    for browser_type in [p.chromium]:
        browser = await browser_type.launch(headless=False, proxy=proxy_obj, channel='chrome')
        context = await browser.new_context(user_agent=user_agent)
        page = await context.new_page()
        
        await context.add_cookies(cookie_object)
        await page.goto(TARGET_URL)
        await browser.close()
```

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/pim97/undetected-playwright-python-bypass-cloudflare.git
    cd repo-name
    ```

2. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Install Playwright browsers:**

    ```bash
    playwright install
    ```

## Usage

1. **Set your API key and proxy URL:**

    In the script, replace `YOUR_API_KEY_HERE` with your actual API key and update the `proxy_url` with your proxy details:

    ```python
    API_KEY = "API_KEY_HERE"
    TARGET_URL = "https://"
    PROXY_URL = 'http://user:pass@host:ip'
    ```

2. **Run the script:**

    ```bash
    python script.py
    ```

    This will execute the script, sending a POST request to the API, extracting the cookie and user agent, and using Playwright to set these cookies and user agent in a browser session while navigating to the specified URL.

## Script Breakdown

- **Step 1:** Send a POST request to the API and extract the cookie and user agent from the response.
- **Step 2:** Parse the target URL to extract the domain.
- **Step 3:** Use Playwright to launch a browser, set the extracted cookie and user agent, and navigate to the specified URL through the provided proxy. 

## Legal and Ethical Considerations

It's crucial to adhere to legal and ethical guidelines when conducting web scraping. Respect the website's terms of service and scraping policies. Ensure that the use of the extracted data complies with all relevant laws and regulations, especially concerning data privacy and intellectual property rights. 🚫⚖️

*Disclaimer: This guide on web scraping is intended for educational and informational purposes only. Engage in responsible web scraping practices and adhere to the terms and conditions of the targeted website.* 📚🔍
