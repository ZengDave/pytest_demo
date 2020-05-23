from ..common.sing_driver import SingleDriver
from ..business.user import UserAction

driver = SingleDriver()
user_action = UserAction()


def test_login():
    #用户登录
    user_action.user_login('testuser5','123456')

    #设置断言
    url = driver.current_url #获取当前网页url
    assert url == 'http://39.107.96.138:3000/', '应该跳转到首页'

    user = driver.find_element_by_xpath('//span[@class="user_name"]/a[@class="dark"]').text
    assert user == 'testuser5', '用户名应该为testuser5'


# def test_register():
#     user_action.user_register()
#
#     url = driver.current_url
#     assert url == 'http://39.107.96.138:3000/signup', '进入注册页面'
