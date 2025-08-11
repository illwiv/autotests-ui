from components.base_component import BaseComponent
from playwright.sync_api import Page

from elements.input import Input


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = Input(page, locator='login-form-email-input', name='Email input')
        self.password_input = Input(page, locator='login-form-password-input', name='Password input')

    def fill(self, email: str, password: str):
        self.email_input.fill(value=email)
        self.password_input.fill(value=password)

    def check_visible(self, email: str, password: str):
        self.email_input.check_visible()
        self.password_input.check_visible()
