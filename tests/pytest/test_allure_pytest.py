import allure


def open_browser():
    with allure.step('Testing allure feature'):
        pass
    with allure.step('Testing allure feature2'):
        pass
    with allure.step('Testing allure feature3'):
        pass

def close_browser():
    with allure.step('Testing allure feature'):
        pass
    with allure.step('Testing allure feature2'):
        pass
    with allure.step('Testing allure feature3'):
        pass

def create_course(title: str):
    with allure.step(f'Testing allure feature {title}'):
        pass
    with allure.step('Testing allure feature2'):
        pass
    with allure.step('Testing allure feature3'):
        pass