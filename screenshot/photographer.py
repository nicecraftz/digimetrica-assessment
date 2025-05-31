from urllib.parse import urlparse
from playwright.sync_api import sync_playwright

SCREENSHOT_NAME_FORMAT = "screenshot_$url$.jpg"

def safe_url(url: str) -> str:
    parsed = urlparse(url)
    return parsed.netloc

def screenshot(page_link: str, output_folder: str):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        page.goto(url=page_link, wait_until="domcontentloaded", referer="alessandrocalista.it")
        page.screenshot(type="jpeg", path=f"{output_folder}/{SCREENSHOT_NAME_FORMAT.replace('$url$', safe_url(page_link))}", full_page=True)

        page.close()
        context.close()
        browser.close()
