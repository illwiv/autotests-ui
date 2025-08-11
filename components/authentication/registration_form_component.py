from components.base_component import BaseComponent
from playwright.sync_api import Page
import allure
from elements.input import Input


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = Input(page, locator='registration-form-email-input', name='Email input')
        self.username_input = Input(page, locator='registration-form-username-input', name='Username input')
        self.password_input = Input(page, locator='registration-form-password-input', name='Password input')

    @allure.step("Fill login form")
    def fill(self, email: str, username: str, password: str):
        self.email_input.fill(value=email)
        self.username_input.fill(value=username)
        self.password_input.fill(value=password)

    @allure.step("Check visible registration form")
    def check_visible(self, email: str, username: str, password: str):
        self.email_input.check_visible()
        self.email_input.check_have_value(email)

        self.username_input.check_visible()
        self.username_input.check_have_value(username)

        self.password_input.check_visible()
        self.password_input.check_have_value(password)
