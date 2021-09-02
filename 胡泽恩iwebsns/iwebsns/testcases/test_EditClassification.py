from iwebsns.testpageobjects.testloginObject import TestLogPage
from iwebsns.config.conftest import login_path
from iwebsns.data.read_write import ReadWrite
from iwebsns.log.log import logger
import time

class Test_Editclass:
    def test_1_Editclass(self,test_logsystem):
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
        self.page1.click_logclass()
        time.sleep(1)
        self.page1.click_edit()
        self.page1.Type_edit("handsome")
        time.sleep(2)
        self.page1.click_save_type_edit()
        try:
            time.sleep(1)
            assert "handsome" in self.page1.check_edit
            print("测试用例成功：成功修改分类")
        except AssertionError:
            print("测试用例失败：未修改分类")
            logger.info("验证用户成功修改分类......")

    def test_2_Editclass(self, test_logsystem):
        self.page1 = TestLogPage(test_logsystem)
        self.page1.click_edit()
        self.page1.Type_edit("")
        self.page1.click_save_type_edit()
        try:
            assert "输入内容不能为空" in self.page1.edit
            print("测试用例成功：成功弹出弹窗")
        except AssertionError:
            print("测试用例失败：成功修改分类")
            logger.info("验证用户修改失败弹出弹窗信息......")