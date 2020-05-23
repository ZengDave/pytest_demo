from ..business.user import UserAction
from ..common.sing_driver import SingleDriver
from ..business.topic import TopicAction
from ..business.viewmange import ViewMange
from ..pom.topicpage import TopicPage
from ..business.usercenter import UserCenter
import pytest

driver = SingleDriver()
topic = TopicAction()
user = UserAction()
view = ViewMange()
topicpage=TopicPage()
user_center=UserCenter()


@pytest.fixture(scope='module', autouse=True)
def module():
    # 用户登录,每个操作需要用户先登录
    user.user_login('testuser5', '123456')
    yield
    driver.quit()


@pytest.fixture(autouse=True)
def func():
    print('______________func setup ___________')
    yield
    print('______________func teardown ___________')


def test_create_topic():
    # 跳转创建话题页面
    view.go_to_newtopic_page()

    # 发帖
    topic.add_topic('ask', 'pytest自动化发帖测试测试+++++', 'hello')

    # 标题和内容添加断言
    title_text = topicpage.title_text
    assert title_text == 'pytest自动化发帖测试测试+++++'
    content_text = topicpage.content_text
    assert content_text == 'hello'

def test_update_topic():
    view.go_to_home_page()#回到主页面
    view.go_to_user_center('testuser5')#进入用户中心
    user_center.click_current_create_topic_by_index(0)#选择最近话题
    topicpage.click_edit_icon()#进入编辑页面
    topic.update_topic('ask', 'pytest自动化发帖测试修改成功', 'helloworld')
