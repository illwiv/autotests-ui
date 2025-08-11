import pytest


@pytest.mark.smoke
def test_smoke_case():
    pass


@pytest.mark.smoke
def test_regression_case():
    pass


@pytest.mark.smoke
class TestSuite:
    def test_case_1(self):
        pass

    def test_case_2(self):
        pass


@pytest.mark.smoke
class TestUserAuth:
    @pytest.mark.smoke
    def test_login(self):
        pass

    @pytest.mark.slow
    def test_password_reset(self):
        pass

    def test_logout(self):
        pass


@pytest.mark.smoke
@pytest.mark.critical
def test_critical_login():
    pass


class TestUserInterface:
    @pytest.mark.smoke
    @pytest.mark.critical
    def test_login_button(self):
        pass

    @pytest.mark.smoke
    def test_forgot_password_link(self):
        pass

    @pytest.mark.smoke
    def test_signup_form(self):
        pass
