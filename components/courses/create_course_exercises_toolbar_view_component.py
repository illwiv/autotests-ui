from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

from elements.button import Button
from elements.text import Text


class CreateCourseExercisesToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, locator='create-course-exercises-box-toolbar-title-text', name='title')
        self.create_button = Button(page, locator='create-course-exercises-box-toolbar-create-exercise-button',
                                    name='create-exercise-button')

    def check_visible(self):
        self.title.check_visible()
        self.title.check_have_text('Exercises')
        self.create_button.check_visible()

    def click_create_exercise_button(self):
        self.create_button.click()
