from playwright.sync_api import sync_playwright, expect
from tools.routers import AppRoute
from config import settings

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(
        headless=settings.headless,
        timeout=10000
    )
    page = browser.new_page()

    page.goto(AppRoute.REGISTRATION)

    reg_button = page.get_by_test_id('registration-page-registration-button')
    expect(reg_button).to_be_disabled()

    email_input = page.get_by_test_id('registration-form-email-input') \
        .locator('input')
    email_input.fill(settings.test_user.email)

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill(settings.test_user.username)

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill(settings.test_user.password)

    expect(reg_button).to_be_enabled()