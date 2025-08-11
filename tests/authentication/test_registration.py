import pytest
import allure
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.tags import AllureTags
from tools.allure.epics import AllureEpic
from tools.allure.stories import AllureStory
from tools.allure.features import AllureFeature
from allure_commons.types import Severity


@pytest.mark.regression
@pytest.mark.registration
@allure.tag(AllureTags.REGISTRATION, AllureTags.REGRESSION)
@allure.epic(AllureEpic.LSM)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
@allure.parent_suite(AllureEpic.LSM)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.REGISTRATION)
class TestRegistration:
    @allure.title('Registration with correct email, username and password')
    @allure.severity(Severity.BLOCKER)
    def test_successful_registration(self, registration_page: RegistrationPage, dashboard_page: DashboardPage):
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_page.registration_form.fill(email="user@gmail.com", username="username", password="password")
        registration_page.registration_form.check_visible(email="user@gmail.com", username="username",
                                                          password="password")
        registration_page.click_registration_button()
        dashboard_page.dashboard_toolbar_view.check_visible()
