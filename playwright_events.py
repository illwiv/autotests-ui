from playwright.sync_api import sync_playwright, Request, Response
from config import settings
from tools.routers import AppRoute


def log_request(request: Request):
    print(f'Request: {request.url}')


def log_response(response: Response):
    print(f'Response: {response.url}, status: {response.status} {response.status_text}')

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=settings.headless, timeout=10000)
    page = browser.new_page()

    page.goto(AppRoute.LOGIN)

    page.on('request', log_request)
    page.remove_listener('request', log_request)
    page.on('response', log_response)
