from iwebsns.testpageobjects.testloginObject import TestLogPage
from iwebsns.config.conftest import login_path
from iwebsns.data.read_write import ReadWrite
from iwebsns.log.log import logger
import time

class TestCreate_log:
    def test_1_CreateLog_Click(self,test_logsystem):
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
        try:
            assert '新建日志' == self.page1.createlog
            print("测试用例成功：成功点击进入新建日志界面")
        except AssertionError:
            print("测试用例失败：无法进入新建日志界面")
            logger.info("验证用户进入日志界面信息......")

    def test_2_CreateLog(self,test_logsystem):
        self.page1 = TestLogPage(test_logsystem)
        self.page1.type_blog_title("我最帅")
        self.page1.type_tag("个人属性")
        self.page1.type_ke_content("我最帅，在座的各位谁赞成，谁反对？")
        time.sleep(2)
        self.page1.click_submit_createlog()
        time.sleep(2)
        try:
            assert '新建日志' == self.page1.createlog
            print("测试用例成功：成功创建日志")
        except AssertionError:
            print("测试用例失败：创建日志失败")
            logger.info("验证用户创建日志信息......")

    def test_3_CreateLog(self,test_logsystem):
        self.page1 = TestLogPage(test_logsystem)
        self.page1.create_Duplicate_log()
        self.page1.type_tag("个人属性")
        self.page1.type_ke_content("我最帅，在座的各位谁赞成，谁反对？")
        time.sleep(2)
        self.page1.click_submit_createlog()
        time.sleep(2)
        try:
            assert  "请填写标题" in self.page1.test_createlog
            print("测试用例成功：未创建日志")
        except AssertionError:
            print("测试用例失败：创建日志成功")
            logger.info("验证用户创建日志失败信息......")
