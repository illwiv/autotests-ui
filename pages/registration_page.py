from components.authentication.registration_form_component import RegistrationFormComponent
from components.dashboard.dashboard_toolbar_view_component import DashboardToolbarViewComponent
from pages.base_page import BasePage
from playwright.sync_api import Page


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)
        self.dashboard_toolbar_view = DashboardToolbarViewComponent(page)

        self.reg_button = page.get_by_test_id('registration-page-registration-button')
        self.login_link = page.get_by_test_id('registration-page-login-link')

    def click_registration_button(self):
        self.reg_button.click()

    def click_login_link(self):
        self.login_link.click()
