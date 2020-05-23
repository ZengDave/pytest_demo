from ..common.sing_driver import SingleDriver


class TopicPage:

    def __init__(self):
        self.driver = SingleDriver()

    def click_edit_icon(self):
        self.driver.find_element_by_css_selector('i[title="编辑"]').click()

    @property
    def title_text(self):
        return self.driver.find_element_by_css_selector('span[class="topic_full_title"]').text

    @property
    def content_text(self):
        return self.driver.find_element_by_css_selector('div[class="markdown-text"]').text
