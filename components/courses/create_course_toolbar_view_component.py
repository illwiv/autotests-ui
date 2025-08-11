from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

from elements.button import Button
from elements.text import Text


class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, locator='create-course-toolbar-title-text', name='title')
        self.button = Button(page, locator='create-course-toolbar-create-course-button',
                             name='create-course-toolbar-button')

    def check_visible(self, is_create_course_disable: bool = True):
        self.title.check_visible()
        self.title.check_have_text('Create course')

        if is_create_course_disable:
            self.button.check_disabled()

        if not is_create_course_disable:
            self.button.check_visible()

    def click_create_course_button(self):
        self.button.click()
