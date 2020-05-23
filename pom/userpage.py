from ..common.sing_driver import SingleDriver

class UserPage:

    def __init__(self):
        self.driver=SingleDriver()

    @property
    def username_input(self):
        return self.driver.find_element_by_css_selector('#name')

    @property
    def password_input(self):
        return self.driver.find_element_by_css_selector('#pass')

    @property
    def login_result(self):
        return self.driver.find_element_by_css_selector('div[class="alert alert-error"]>strong').text