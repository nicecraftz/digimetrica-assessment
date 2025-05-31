import requests
from urllib.parse import urlparse
from playwright.sync_api import sync_playwright, TimeoutError
import logging

SCREENSHOT_NAME_FORMAT = "screenshot_$url$.jpg"
logging.basicConfig(level=logging.ERROR)

def netloc_from_url(url: str) -> str:
    parsed = urlparse(url)
    return parsed.netloc

def check_reachable(url: str) -> bool:
    try:
        response = requests.head(url, timeout=5)
        return True
    except requests.RequestException:
        return False

def is_valid_and_reachable(url: str) -> bool:
    if url is None or len(url) == 0:
        return False

    parsed = urlparse(url)
    if not parsed.scheme and not parsed.netloc:
        return False
    return check_reachable(url)

def screenshot(page_link: str, output_folder: str) -> tuple[bool,str,str]:
    with sync_playwright() as p:
        if not is_valid_and_reachable(page_link):
            return (False, "Invalid URL", "")

        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        output = output_folder + "/" + SCREENSHOT_NAME_FORMAT.replace('$url$', netloc_from_url(page_link))

        try:
            page.goto(url=page_link, wait_until="domcontentloaded", referer=page_link)
            page.screenshot(type="jpeg", path=output, full_page=True)
        except TimeoutError as _:
            logging.error("La pagina ha impiegato troppo tempo per rispondere", exc_info=True)
            return (False, "Timed Out", "")

        page.close()
        context.close()
        browser.close()
        return (True, "URL Valido", output)
