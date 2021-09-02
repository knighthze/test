from iwebsns.testpageobjects.testloginObject import TestLogPage
from iwebsns.config.conftest import login_path
from iwebsns.data.read_write import ReadWrite
from iwebsns.log.log import logger
import time

class Test_Searchgroup:
    def test_1(self,test_logsystem):
        self.page1=TestLogPage(test_logsystem)
        file = ReadWrite(login_path)
        userlist = file.read()
        for user in userlist:
            self.page1.type_login_email(user[0])
            self.page1.type_login_pws(user[1])
            self.page1.click_loginsubm()
        self.page1.click_group()
        self.page1.click_searchgroup()
        self.page1.type_searchgroupname("沪上青玉流")
        self.page1.click_searchsubmit()
        time.sleep(2)
        try:
            assert "沪上青玉流" in self.page1.check_creategroup
            print("测试用例成功：搜索成功")
        except AssertionError:
            print("测试用例失败：搜索失败")
            logger.info("验证用户成功搜索群组信息......")


    def test_2(self,test_logsystem):
        self.page1 = TestLogPage(test_logsystem)
        self.page1.click_searchgroup()
        time.sleep(2)
        self.page1.click_searchsubmit()
        try:
            assert "请输入搜索内容" in self.page1.test_creategroup
            print("测试用例成功：正确弹出相应提示")
        except AssertionError:
            print("测试用例失败：成功搜索")
            logger.info("验证用户搜索群组失败弹出弹窗信息......")