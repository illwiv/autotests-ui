from playwright.sync_api import sync_playwright
from config import settings
from tools.routers import AppRoute

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=settings.headless, timeout=10000)
    page = browser.new_page()

    page.goto(AppRoute.LOGIN)

    registration_link = page.get_by_test_id('login-page-registration-link')
    registration_link.hover()
