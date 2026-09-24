from playwright.sync_api import sync_playwright
import time

URL = "https://movies-dataset-g68dfeaf04.streamlit.app/"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(URL, wait_until="domcontentloaded", timeout=60000)
    time.sleep(15)

    wake_btn = page.locator("text=Yes, get this app back up!")
    if wake_btn.count() > 0:
        wake_btn.first.click()
        print("App estaba dormida → despertando...")
        page.wait_for_load_state("networkidle", timeout=120000)
    else:
        print("App ya estaba activa.")

    browser.close()   