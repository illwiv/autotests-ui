from components.base_component import BaseComponent
from playwright.sync_api import Page
import allure
from components.courses.course_view_menu_component import CourseViewMenuComponent
from elements.Image import Image
from elements.text import Text


class CourseViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu = CourseViewMenuComponent(page)

        self.title = Text(page, locator='course-widget-title-text', name='title course view')
        self.image = Image(page, locator='course-preview-image', name='course preview image')
        self.max_score_text = Text(page, locator='course-max-score-info-row-view-text', name='max score course view')
        self.min_score_text = Text(page, locator='course-min-score-info-row-view-text', name='min score course view')
        self.estimated_time_text = Text(page, locator='course-estimated-time-info-row-view-text',
                                        name='estimated time course view')

    @allure.step('Check visible course view at index "{index}"')
    def check_visible(
            self,
            index: int,
            title: str,
            max_score: str,
            min_score: str,
            estimated_time: str
    ):
        self.image.check_visible(nth=index)

        self.title.check_visible(nth=index)
        self.title.check_have_text(title, nth=index)

        self.max_score_text.check_visible(nth=index)
        self.max_score_text.check_have_text(f"Max score: {max_score}", nth=index)

        self.min_score_text.check_visible(nth=index)
        self.min_score_text.check_have_text(f"Min score: {min_score}", nth=index)

        self.estimated_time_text.check_visible(nth=index)
        self.estimated_time_text.check_have_text(f"Estimated time: {estimated_time}", nth=index)
