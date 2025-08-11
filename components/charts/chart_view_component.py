from components.base_component import BaseComponent
from playwright.sync_api import Page
import allure
from elements.Image import Image
from elements.text import Text


class ChartViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str, chart_type: str):
        super().__init__(page)

        self.title = Text(page, locator=f'{identifier}-widget-title-text', name='chart title')
        self.chart = Image(page, locator=f'{identifier}-{chart_type}-chart', name='chart')

    @allure.step('Checking visibility title "{title}" and chart')
    def check_visible(self, title: str):
        self.title.check_visible()
        self.title.check_have_text(title)
        self.chart.check_visible()
