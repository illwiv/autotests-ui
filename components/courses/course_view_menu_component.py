from components.base_component import BaseComponent
from playwright.sync_api import Page
import allure
from elements.button import Button


class CourseViewMenuComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu_button = Button(page, locator='course-view-menu-button', name='course-view-menu-button')
        self.edit_menu_button = Button(page, locator='course-view-edit-menu-item', name='course-view-edit-menu-item')
        self.delete_menu_button = Button(page, locator='course-view-delete-menu-item',
                                         name='course-view-delete-menu-item')

    @allure.step('Open course menu at index "{index}" and click edit button')
    def click_edit(self, index: int):
        self.menu_button.click(nth=index)

        self.edit_menu_button.check_visible(nth=index)
        self.edit_menu_button.click(nth=index)

    @allure.step('Open course menu at index "{index}"  and click delete button')
    def click_delete(self, index: int):
        self.menu_button.click(nth=index)

        self.delete_menu_button.check_visible(nth=index)
        self.delete_menu_button.click(nth=index)
