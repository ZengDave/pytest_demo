from ..common.sing_driver import SingleDriver


class ViewMange:


    def __init__(self):
        self.driver=SingleDriver()

    """
    跳转创建话题页面
    """
    def go_to_newtopic_page(self):
        self.driver.find_element_by_css_selector('a[id="create_topic_btn"]').click()

    # 回到主页面
    def go_to_home_page(self):
        self.driver.get('http://39.107.96.138:3000/')

    # 跳转用户界面
    def go_to_user_center(self, username):
        self.driver.get("http://39.107.96.138:3000/user/" + username)