from ..common.sing_driver import SingleDriver
from ..pom.userpage import UserPage

userpage = UserPage()

class UserAction:


    """
    用户登录
    用户注册
    """

    def __init__(self):
        self.driver=SingleDriver()

    # 用户登录
    def user_login(self,username,password):
        url = 'http://39.107.96.138:3000/signin'
        self.driver.get(url)
        self.driver.find_element_by_xpath('//input[@id="name"]').send_keys(username)
        self.driver.find_element_by_xpath('//input[@id="pass"]').send_keys(password)
        self.driver.find_element_by_xpath('//input[@type="submit"]').click()

    # 用户注册
    def user_register(self,username,pw,repw,email):
        url = 'http://39.107.96.138:3000/signin'
        self.driver.get(url)
        self.driver.find_element_by_xpath('//ul[@class="nav pull-right"]/li[5]/a').click()
        self.driver.find_element_by_xpath('//input[@id="loginname"]').send_keys(username)
        self.driver.find_element_by_xpath('//input[@id="pass"]').send_keys(pw)
        self.driver.find_element_by_xpath('//input[@id="re_pass"]').send_keys(repw)
        self.driver.find_element_by_xpath('//input[@id="email"]').send_keys(email)
        self.driver.find_element_by_xpath('//input[@value="注册"]').click()

