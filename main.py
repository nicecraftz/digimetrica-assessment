import requests
import urllib.parse
from playwright.sync_api import Page, sync_playwright
import streamlit
import json

DATA = "data.json"
RESOURCES_FOLDER = "output"
SCREENSHOT_NAME_FORMAT = "screenshot_$url$.jpg"

def safe_url(url: str) -> str:
    parsed = urllib.parse.urlparse(url)
    return parsed.netloc

def screenshot_page(page: Page, page_link: str):
    page.goto(url=page_link, wait_until="domcontentloaded", referer="alessandrocalista.it")
    page.screenshot(type="jpeg", path=f"{RESOURCES_FOLDER}/{SCREENSHOT_NAME_FORMAT.replace('$url$', safe_url(page_link))}", full_page=True)

def main():
    urls = []
    with open(DATA, "r", encoding="utf-8") as file:
        file_data = json.load(file)
        urls = set(file_data["urls"])

    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        for url in urls:
            screenshot_page(page, url)
        page.close()
        context.close()
        browser.close()

if __name__ == "__main__":
    main()
