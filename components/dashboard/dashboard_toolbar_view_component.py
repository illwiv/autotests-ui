from components.base_component import BaseComponent
from playwright.sync_api import Page

from elements.text import Text


class DashboardToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, locator='dashboard-toolbar-title-text', name='Dashboard title')

    def check_visible(self):
        self.title.check_visible()
        self.title.check_have_text('Dashboard')
