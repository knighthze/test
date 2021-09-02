from iwebsns.testpageobjects.testloginObject import TestLogPage
from iwebsns.config.conftest import login_path
from iwebsns.data.read_write import ReadWrite
from iwebsns.log.log import logger
import time

class TestAddClassification:
    def test_1_ClickAddClass(self,test_logsystem):
        self.page1 = TestLogPage(test_logsystem)
        file = ReadWrite(login_path)
        userlist = file.read()
        for user in userlist:
            self.page1.type_login_email(user[0])
            self.page1.type_login_pws(user[1])
            self.page1.click_loginsubm()
            time.sleep(2)
        self.page1.click_log()
        time.sleep(2)
        self.page1.click_createlog()
        time.sleep(1)
        self.page1.click_addclassification()
        try:
            assert "new_sort_name" in self.page1.new_sort_name
            print("测试用例成功：成功显示文本框")
        except AssertionError:
            print("测试用例失败：选项失效")
        logger.info("验证用户点击添加分类信息......")

    def test_2_TypeAddClass(self,test_logsystem):
        self.page1 = TestLogPage(test_logsystem)
        self.page1.type_new_sort_name("smart")
        self.page1.click_save_sort_name()
        try:
            self.page1.click_logclass()
            time.sleep(2)
            assert "smart" in self.page1.check_logclass
            print("测试用例成功：创建成功")
        except AssertionError:
            print("测试用例失败：创建失败")
        logger.info("验证用户创建分类信息......")

    def test_3_back(self,test_logsystem):
        self.page1 = TestLogPage(test_logsystem)
        self.page1.click_back()
        try:
            assert "添加分类" in self.page1.addclassification
            print("测试用例成功：返回成功")
        except AssertionError:
            print("测试用例失败：返回失败")

    def test_4_TypeAddClass(self,test_logsystem):
        self.page1 = TestLogPage(test_logsystem)

        self.page1.click_addclassification()
        self.page1.type_new_sort_name("")
        self.page1.click_save_sort_name()
        try:
            assert "请填写信息" in self.page1.test_logclass
            print("测试用例成功：弹出对应提示，创建失败")
        except AssertionError:
            print("测试用例失败：创建成功")
        logger.info("验证用户创建分类信息......")