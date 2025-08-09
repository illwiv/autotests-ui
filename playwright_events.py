from playwright.sync_api import sync_playwright, Request, Response

def log_request(request: Request):
    print(f'Request: {request.url}')


def log_response(response: Response):
    print(f'Response: {response.url}, status: {response.status} {response.status_text}')

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, timeout=10000)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    page.on('request', log_request)
    page.remove_listener('request', log_request)
    page.on('response', log_response)
