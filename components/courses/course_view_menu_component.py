from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

from elements.button import Button


class CourseViewMenuComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu_button = Button(page, locator='course-view-menu-button', name='course-view-menu-button')
        self.edit_menu_button = Button(page, locator='course-view-edit-menu-item', name='course-view-edit-menu-item')
        self.delete_menu_button = Button(page, locator='course-view-delete-menu-item',
                                         name='course-view-delete-menu-item')

    def click_edit(self):
        self.menu_button.click()

        self.edit_menu_button.check_visible()
        self.edit_menu_button.click()

    def click_delete(self, index: int):
        self.menu_button.click()

        self.delete_menu_button.check_visible()
        self.delete_menu_button.click()
