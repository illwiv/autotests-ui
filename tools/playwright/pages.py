import allure
from playwright.sync_api import Playwright, Page
from config import settings


def init_playwright_page(
        playwright: Playwright,
        test_name: str,
        storage_state: str | None = None) -> Page:
    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context(base_url=settings.get_base_url(), storage_state=storage_state, record_video_dir=settings.videos_dir)
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    yield page

    context.tracing.stop(path=settings.tracing_dir.joinpath(f'{test_name}.zip'))
    browser.close()

    allure.attach.file(settings.tracing_dir.joinpath(f'{test_name}.zip'), name=f'{test_name}_trace', extension='zip')
    allure.attach.file(page.video.path(), name=f'{test_name}_trace', extension='mp4')
