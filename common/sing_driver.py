from selenium import webdriver

class SingleDriver:
    """
    单例模式，同意管理浏览器的实例
    """

    __instance=None

    def __new__(cls, *args, **kwargs):
        """
        new 对象会调用
        :param args:
        :param kwargs:
        :return:
        """
        if cls.__instance is None:
            cls.__instance=webdriver.Chrome()
            cls.__instance.implicitly_wait(10)
            # cls.__instance.set_page_load_timeout(10)
            # cls.__instance.maximize_window()
        return cls.__instance

if __name__ == '__main__':
    driver1=SingleDriver()
    driver2=SingleDriver()
    print(driver1==driver2)
