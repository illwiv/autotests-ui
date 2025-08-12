from playwright.sync_api import sync_playwright
from tools.routers import AppRoute
from config import settings

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=settings.headless)
    page = browser.new_page()

    page.goto(AppRoute.LOGIN,
              wait_until='networkidle',
              )

    # unknown = page.locator("#unknown")
    # expect(unknown).to_be_visible()

    # login_button = page.get_by_test_id('login-page-login-button')
    # login_button.fill('hi')

    new_text = 'Hi'
    page.evaluate(
        """
        (text) => {
            const title = document.getElementById('authentication-ui-course-title-text')
            title.textContent = text
        }
        """,
        new_text
    )
