from ..common.sing_driver import SingleDriver

class EditTopicPage:

    def __init__(self):
        self.driver = SingleDriver()


    @property
    def breadcrumb_text(self):
        return self.driver.find_element_by_css_selector('div.header>ol>li.active').text

    @property
    def error_msg_text(self):
        return self.driver.find_element_by_css_selector('div[class="alert alert-error"] > strong').text

    @property
    def alert_msg_text(self):
        alert = self.driver.switch_to.alert
        text = alert.text
        alert.accept()
        return text
