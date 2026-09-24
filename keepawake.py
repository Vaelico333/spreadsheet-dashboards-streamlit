from playwright.sync_api import sync_playwright
import time

URL = "https://movies-dataset-g68dfeaf04.streamlit.app/"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(URL, wait_until="domcontentloaded", timeout=60000)

    # Esperar a que la página renderice el botón (o a que la app ya esté activa)
    wake_btn = page.locator('[data-testid="wakeup-button-owner"]')
    try:
        wake_btn.wait_for(state="visible", timeout=30000)
        print("App dormida → clickeando botón de wake...")
        wake_btn.click()

        # Esperar a que el botón desaparezca (la app está arrancando)
        page.wait_for_selector(
            '[data-testid="wakeup-button-owner"]',
            state="detached",
            timeout=120000
        )
        print("Botón desapareció → app arrancando...")

        # Esperar a que el contenedor de la app renderice
        page.wait_for_selector(
            "div[data-testid='stAppViewContainer']",
            timeout=120000
        )
        print("✅ App activa y renderizada.")

    except Exception as e:
        # Si el botón no aparece en 30s, la app ya estaba activa
        if "Timeout" in str(type(e).__name__) or "timeout" in str(e).lower():
            print("No hay botón de wake → app ya estaba activa ✅")
        else:
            raise

    # Mantener la sesión abierta unos segundos para que se registre
    time.sleep(10)
    browser.close()