from playwright.sync_api import sync_playwright, expect
from config import settings
from tools.routers import AppRoute

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=settings.headless, timeout=10000)
    page = browser.new_page()

    page.goto(AppRoute.LOGIN)

    login_button = page.get_by_test_id('login-page-login-button')
    expect(login_button).to_be_disabled()