# Proxy User Agent and Cookie Setter

This repository contains a Python script that sends a POST request to an API, extracts the cookie and user agent, and uses Playwright to set these cookies and user agent in a browser session while navigating to a specified URL through a proxy.

## Prerequisites

- Python 3.7+
- [Playwright](https://playwright.dev/python/docs/intro) for Python
- Required Python packages (listed in `requirements.txt`)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/pim97/playwright-python-solve-cloudflare
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
    url = "https://publisher.scrappey.com/api/v1?key=YOUR_API_KEY_HERE"
    proxy_url = 'http://user:pass@host:ip'
    ```

2. **Run the script:**

    ```bash
    python script_name.py
    ```

    This will execute the script, sending a POST request to the API, extracting the cookie and user agent, and using Playwright to set these cookies and user agent in a browser session while navigating to the specified URL.

## Script Breakdown

- **Step 1:** Send a POST request to the API and extract the cookie and user agent from the response.
- **Step 2:** Parse the target URL to extract the domain.
- **Step 3:** Use Playwright to launch a browser, set the extracted cookie and user agent, and navigate to the specified URL through the provided proxy.

### Functions

- **`parse_cookie_string(cookie_string)`**: Parses the cookie string into a list of cookie dictionaries.
- **`main()`**: The main asynchronous function that uses Playwright to launch the browser, set cookies and user agent, and navigate to the target URL.

## Example Response Structure

Make sure to adjust the `cookie_string` and `user_agent` extraction according to the actual structure of the response from your API.

```json
{
  "solution": {
    "cookieString": "cookie_name=cookie_value; another_cookie=another_value",
    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
  }
}
