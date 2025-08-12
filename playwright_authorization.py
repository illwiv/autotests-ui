from playwright.sync_api import sync_playwright, expect
from config import settings

from tools.routers import AppRoute

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(
        headless=settings.headless,
        timeout=10000
    )
    page = browser.new_page()

    page.goto(AppRoute.LOGIN)
    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    email_input.fill(settings.test_user.email)

    password_input = page.get_by_test_id('login-form-password-input').locator('input')
    password_input.fill(settings.test_user.password)

    login_button = page.get_by_test_id('login-page-login-button')
    login_button.click()

    wrong_email_or_password_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')
    expect(wrong_email_or_password_alert).to_be_visible()
    expect(wrong_email_or_password_alert).to_have_text('Wrong email or password')
