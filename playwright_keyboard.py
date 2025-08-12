from playwright.sync_api import sync_playwright
from config import settings

from tools.routers import AppRoute

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=settings.headless)
    page = browser.new_page()

    page.goto(AppRoute.LOGIN)

    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    email_input.focus()

    for char in settings.test_user.username:
        page.keyboard.type(char)

    page.keyboard.press('ControlOrMeta+A')
