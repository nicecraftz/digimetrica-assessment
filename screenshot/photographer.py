import requests
from urllib.parse import urlparse
from playwright.sync_api import sync_playwright, TimeoutError
import logging

SCREENSHOT_NAME_FORMAT = "screenshot_$url$.jpg"
logging.basicConfig(level=logging.ERROR)

def safe_url(url: str) -> str:
    parsed = urlparse(url)
    return parsed.netloc

def is_reachable(url: str) -> bool:
    try:
        response = requests.head(url, timeout=5)
        return True
    except requests.RequestException:
        return False

def is_valid_and_reachable(url: str) -> bool:
    parsed = urlparse(url)
    if not parsed.scheme and not parsed.netloc:
        return False
    return is_reachable(url)

def screenshot(page_link: str, output_folder: str) -> str:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        output = output_folder + "/" + SCREENSHOT_NAME_FORMAT.replace('$url$', safe_url(page_link))

        try:
            page.goto(url=page_link, wait_until="domcontentloaded", referer="alessandrocalista.it")
            page.screenshot(type="jpeg", path=output, full_page=True)
        except TimeoutError as _:
            logging.error("La pagina ha impiegato troppo tempo per rispondere", exc_info=True)

        page.close()
        context.close()
        browser.close()
        return output
