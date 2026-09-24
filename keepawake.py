from playwright.sync_api import sync_playwright
import time

URL = "https://movies-dataset-g68dfeaf04.streamlit.app/"

def wake_app():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(URL, wait_until="domcontentloaded", timeout=60000)

        wake_btn = page.locator(selector='button[data-testid="wakeup-button-owner"]')
        try:
            time.sleep(5)
            app_div = page.locator('div[class="_streamlitAppContainer_1j65n_1"]')
            if app_div.count() > 0:
                print("App activa → cerrando explorador ✅")
                return

            wake_btn.wait_for(state="visible", timeout=10000)
            print("App dormida → clicando botón de wake...")
            wake_btn.click()

            page.wait_for_selector(
                'button[data-testid="wakeup-button-owner"]',
                state="hidden",
                timeout=60000
            )
            print("Botón desapareció → app arrancando...")

            page.wait_for_selector(
                'div[class="_streamlitAppContainer_1j65n_1"]',
                timeout=60000
            )
            print("✅ App activa y renderizada.")
            time.sleep(5)
            return

        except Exception as e:
            if "Timeout" in str(type(e).__name__) or "timeout" in str(e).lower():
                print(f"No hay botón de wake → app ya estaba activa ✅\nrazón: {e}")
            else:
                raise e

    

if __name__ == '__main__':
    wake_app()