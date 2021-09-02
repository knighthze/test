from iwebsns.testpageobjects.testloginObject import TestLogPage
from iwebsns.config.conftest import login_path
from iwebsns.data.read_write import ReadWrite
from iwebsns.log.log import logger
import time

class TestLogin:
    def test_1_login(self,test_logsystem):
        self.page1=TestLogPage(test_logsystem)
        file=ReadWrite(login_path)
        userlist=file.read()
        for user in userlist:
            self.page1.type_login_email(user[0])
            self.page1.type_login_pws(user[1])
            self.page1.click_loginsubm()
            time.sleep(3)
            try:
                time.sleep(2)
                assert self.page1.browser.title == "吾之梦的个人首页-聚易社区"
                print("测试用例成功：登录成功！")
            except AssertionError:
                print("测试用例失败：登录失败！")
            logger.info("验证用户登录信息......")

    def test_2_logout(self,test_logsystem):
        self.page1=TestLogPage(test_logsystem)
        self.page1.click_logout()
        try:
            time.sleep(2)
            assert self.page1.browser.title == "聚易社区"
            print("测试用例成功：退出成功！")
        except AssertionError:
            print("测试用例失败:退出失败")
            logger.info("验证用户退出信息......")


    def test_3_login(self,test_logsystem):
        self.page1=TestLogPage(test_logsystem)
        self.page1.type_login_email('knight')
        self.page1.type_login_pws('111111222222')
        self.page1.click_loginsubm()
        try:
            time.sleep(2)
            assert self.page1.browser.title == "聚易社区"
            print("测试用例成功：登录失败！")
            logger.info("验证用户登录失败信息.......")
        except AssertionError:
            print("测试用例失败：异常情况！")
            logger.info("验证用户登录失败信息.......")

