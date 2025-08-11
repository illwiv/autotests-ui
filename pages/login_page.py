from components.authentication.login_form_component import LoginFormComponent
from elements.button import Button
from elements.link import Link
from elements.text import Text
from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.login_form = LoginFormComponent(page)

        self.login_button = Button(page, locator='login-page-login-button', name='Login')
        self.registration_link = Link(page, locator='login-page-registration-link', name='Registration link')
        self.wrong_email_or_password_alert = Text(page, 'login-page-wrong-email-or-password-alert',
                                                  name='Wrong email or password')

    def click_login_button(self):
        self.login_button.click()

    def click_registration_link(self):
        self.registration_link.click()

    def check_visible_wrong_email_or_password_alert(self):
        self.wrong_email_or_password_alert.check_visible()
        self.wrong_email_or_password_alert.check_have_text('Wrong email or password')
