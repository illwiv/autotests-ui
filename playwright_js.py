from playwright.sync_api import sync_playwright, expect
from tools.routers import AppRoute
from config import settings

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=settings.headless)
    page = browser.new_page()

    page.goto(
        AppRoute.LOGIN,
        wait_until='networkidle'
    )

    new_text = 'New text'
    page.evaluate(
        """
        (text) => {
            const title = document.getElementById('authentication-ui-course-title-text')
            title.textContent = text
        }
        """,
        new_text
    )

    expect(page.get_by_test_id('authentication-ui-course-title-text')).to_have_text("New text")
