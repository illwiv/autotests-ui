from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

from elements.button import Button
from elements.input import Input
from elements.text import Text


class CreateCourseExerciseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.delete_exercise_button = Button(page,
                                             locator="create-course-exercise-{index}-box-toolbar-delete-exercise-button",
                                             name='Delete Exercise',
                                             )

        self.subtitle = Text(page, locator="create-course-exercise-{index}-box-toolbar-subtitle-text",
                             name='Exercise form subtitle')
        self.title_input = Input(page, locator="create-course-exercise-form-title-{index}-input",
                                 name='Exercise form input')
        self.description_input = Input(page, locator="create-course-exercise-form-description-{index}-input",
                                       name='Exercise form description')

    def click_delete_button(self, index: int):
        self.delete_exercise_button.click(index=index)

    def check_visible(self, index: int, title: str, description: str):
        self.subtitle.check_visible(index=index)
        self.subtitle.check_have_text(f'#{index + 1} Exercise', index=index)

        self.title_input.check_visible(index=index)
        self.title_input.check_have_value(title, index=index)

        self.title_input.check_visible(index=index)
        self.title_input.check_have_value(description, index=index)

    def fill(self, index: int, title: str, description: str):
        self.title_input.fill(value=title, index=index)
        self.title_input.check_have_value(title, index=index)

        self.description_input.fill(value=description, index=index)
        self.description_input.check_have_value(description, index=index)
