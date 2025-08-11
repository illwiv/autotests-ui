from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

from elements.button import Button


class CourseViewMenuComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu_button = Button('course-view-menu-button')
        self.edit_menu_button = Button('course-view-edit-menu-item')
        self.delete_menu_button = Button('course-view-delete-menu-item')

    def click_edit(self, index: int):
        self.menu_button.click(nth=index)

        self.edit_menu_button.check_visible(nth=index)
        self.edit_menu_button.click(nth=index)

    def click_delete(self, index: int):
        self.menu_button.click(nth=index)

        self.delete_menu_button.check_visible(nth=index)
        self.delete_menu_button.click(nth=index)
