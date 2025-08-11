from playwright.sync_api import Page
from components.base_component import BaseComponent
from components.views.empty_view_component import EmptyViewComponent
from elements.Image import Image
from elements.button import Button
from elements.icon import Icon
from elements.file_input import FileInput
from elements.text import Text


class ImageUploadWidgetComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.preview_empty_view = EmptyViewComponent(page)

        self.preview_image = Image(page, locator='{identifier}-image-upload-widget-preview-image', name='Preview Image')

        self.image_upload_info_icon = Icon(page, locator='{identifier}-image-upload-widget-info-icon',
                                           name='Image Upload Info')
        self.image_upload_info_title = Text(page, locator='{identifier}-image-upload-widget-info-title-text',
                                            name='Image Upload Info Title')
        self.image_upload_info_description = Text(page,
                                                  locator='{identifier}-image-upload-widget-info-description-text',
                                                  name='Image Upload Info Description')

        self.upload_button = Button(page, locator='{identifier}-image-upload-widget-upload-button', name='Upload Image')
        self.remove_button = Button(page, locator='{identifier}-image-upload-widget-remove-button', name='Remove Image')
        self.upload_input = FileInput(page, locator='{identifier}-image-upload-widget-input', name='Upload Input')

    def check_visible(self, is_image_uploaded: bool = False, identifier='create-course-preview'):
        self.image_upload_info_icon.check_visible(identifier=identifier)

        self.image_upload_info_title.check_visible(identifier=identifier)
        self.image_upload_info_title.check_have_text('Tap on "Upload image" button to select file', identifier=identifier,)

        self.image_upload_info_description.check_visible(identifier=identifier,)
        self.image_upload_info_description.check_have_text('Recommended file size 540X300', identifier=identifier,)

        self.upload_button.check_visible(identifier=identifier)

        if is_image_uploaded:
            self.remove_button.check_visible(identifier=identifier)
            self.preview_image.check_visible(identifier=identifier)

        if not is_image_uploaded:
            self.preview_empty_view.check_visible(
                title='No image selected',
                description='Preview of selected image will be displayed here',
                identifier=identifier,
            )

    def click_remove_image_button(self):
        self.remove_button.click()

    def upload_preview_image(self, file: str, identifier='create-course-preview'):
        self.upload_input.set_input_files(file,identifier=identifier)
