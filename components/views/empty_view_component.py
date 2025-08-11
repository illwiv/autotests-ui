from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
import allure
from elements.icon import Icon
from elements.text import Text


class EmptyViewComponent(BaseComponent):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.empty_view_icon = Icon(page, locator='{identifier}-empty-view-icon', name='Empty View Icon')
        self.empty_view_title = Text(page, locator='{identifier}-empty-view-title-text', name='Empty View Title')
        self.empty_view_description = Text(page, locator='{identifier}-empty-view-description-text',
                                           name='Empty View Description')

    @allure.step('Check visible empty view "{title}"')
    def check_visible(self, title: str, description: str, identifier: str):
        self.empty_view_icon.check_visible(identifier=identifier)

        self.empty_view_title.check_visible(identifier=identifier)
        self.empty_view_title.check_have_text(text=title, identifier=identifier)

        self.empty_view_description.check_visible(identifier=identifier)
        self.empty_view_description.check_have_text(text=description, identifier=identifier)
