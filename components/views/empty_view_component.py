from itertools import starmap

from components.base_component import BaseComponent
from playwright.sync_api import Page, expect


class EmptyViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier:str) -> None:
        super().__init__(page)

        self.empty_view_icon = page.get_by_test_id(f'{identifier}-empty-view-icon')
        self.empty_view_title = page.get_by_test_id(f'{identifier}-empty-view-title-text')
        self.empty_view_description = page.get_by_test_id(f'{identifier}-empty-view-description-text')


    def check_visible(self, title: str, description: str):
        expect(self.empty_view_icon).to_be_visible()

        expect(self.empty_view_title).to_be_visible()
        expect(self.empty_view_title).to_have_text(title)

        expect(self.empty_view_description).to_be_visible()
        expect(self.empty_view_description).to_have_text(description)