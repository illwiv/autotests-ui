from typing import Pattern

from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.icon import Icon


class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.icon = Icon(page, locator='{identifier}-drawer-list-item-icon', name='Sidebar icon')
        self.title = Icon(page, locator='{identifier}-drawer-list-item-title-text', name='Sidebar title')
        self.button = Icon(page, locator='{identifier}-drawer-list-item-button', name='Sidebar button')

    def check_visible(self, title: str, identifier: str):
        self.icon.check_visible(identifier=identifier)

        self.title.check_visible(identifier=identifier)
        self.title.check_have_text(text=title, identifier=identifier)

        self.button.check_visible(identifier=identifier)

    def navigate(self, expected_url: Pattern[str], identifier: str):
        self.button.click(identifier=identifier)
        self.check_current_url(expected_url)
