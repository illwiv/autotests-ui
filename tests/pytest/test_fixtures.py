import pytest


@pytest.fixture(autouse=True)
def send_analytics_data():
    print("[AUTOUSE]")


@pytest.fixture(scope='session')
def settings():
    print("[SESSION]")


@pytest.fixture(scope='class')
def user():
    print("[CLASS]")


@pytest.fixture(scope='function')
def browser():
    print("[FUNCTION]")


class TestUserFlow:
    def test_user_can_login(self, settings, user, browser):
        pass

    def test_user_create_course(self, settings, user, browser):
        pass


class TestUserAccount:
    def test_user_create_account(self, settings, user, browser):
        pass
