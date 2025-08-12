from playwright.sync_api import sync_playwright, expect
from tools.routers import AppRoute
from config import settings

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context()
    page = context.new_page()

    page.goto(AppRoute.REGISTRATION)

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill(settings.test_user.email)

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill(settings.test_user.username)

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill(settings.test_user.password)

    reg_button = page.get_by_test_id('registration-page-registration-button')
    reg_button.click()

    page.wait_for_load_state("networkidle")  # без него в json сохраняются данные не авторизованного пользователя

    context.storage_state(path=settings.browser_state_file)

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context(storage_state=settings.browser_state_file)

    page = context.new_page()

    page.goto(AppRoute.COURSES)

    courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_have_text('Courses')

    courses_icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(courses_icon).to_be_visible()

    courses_result = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(courses_result).to_have_text('There is no results')

    courses_pipeline = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(courses_pipeline).to_have_text('Results from the load test pipeline will be displayed here')
