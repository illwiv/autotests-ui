import re

from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.navigation.sidebar_list_item_component import SidebarListItemComponent


class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.logout_list_item = SidebarListItemComponent(page)
        self.courses_list_item = SidebarListItemComponent(page)
        self.dashboard_list_item = SidebarListItemComponent(page)

    def check_visible(self):
        self.logout_list_item.check_visible(title='Logout', identifier='logout')
        self.courses_list_item.check_visible(title='Courses', identifier='courses')
        self.dashboard_list_item.check_visible(title='Dashboard', identifier='dashboard')

    def click_logout(self):
        self.logout_list_item.navigate(re.compile(r".*/#/auth/login"), identifier='logout')

    def click_courses(self):
        self.courses_list_item.navigate(re.compile(r".*/#/courses"), identifier='courses')

    def click_dashboard(self):
        self.dashboard_list_item.navigate(re.compile(r".*/#/dashboard"), identifier='dashboard')
