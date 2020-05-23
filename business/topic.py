from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from ..common.sing_driver import SingleDriver
from selenium.webdriver.common.action_chains import ActionChains


class TopicAction:
    """
    新增话题
    删除话题
    修改话题
    查看话题
    回复话题
    """

    def __init__(self):
        self.driver = SingleDriver()
        self._tab_css = 'select[id="tab-value"]'
        self._title_css = 'textarea[id="title"]'
        self._content_css = 'div[class="CodeMirror-scroll"]'
        self._submit_css = 'input[value="提交"]'

    def __creat_topic(self, tab=None, tittle=None, content=None):
        # 发布话题的模块
        select_tab = self.driver.find_element_by_css_selector(self._tab_css)
        # select_tab.find_element_by_xpath(f'//option[@value="{tab}"]').click()#二次定位
        Select(select_tab).select_by_value(tab)  # 也可以使用这种方式，用的Select里的方法，导包

        # 发布话题的标题
        title_area = self.driver.find_element_by_css_selector(self._title_css)
        title_area.clear()  # 清除标题文本，可用作更新使用
        title_area.send_keys(tittle)  # 传入标题的值

        # 发布话题的文本内容
        content_area = self.driver.find_element_by_css_selector(self._content_css)
        content_area.click()
        actions = ActionChains(self.driver)
        # window下删除这种文本的方法
        actions.move_to_element(content_area) \
            .key_down(Keys.CONTROL) \
            .send_keys('a') \
            .key_up(Keys.CONTROL) \
            .send_keys(Keys.DELETE).perform()
        actions.move_to_element(content_area).send_keys(content).perform()

        # 点击话题发布按钮
        self.driver.find_element_by_css_selector(self._submit_css).click()

    def add_topic(self, tab, title, content):
        self.__creat_topic(tab, title, content)

    def update_topic(self,tab=None, title=None, content=None):
        self.__creat_topic(tab, title, content)

    def del_topic(self):
        pass

    def reply_topic(self):
        pass

    """
    获取发帖错误信息提示
    """

    def errmessage(self):
        return self.driver.find_element_by_css_selector('div[class="alert alert-error"]>strong').text
