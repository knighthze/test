from iwebsns.testpageobjects.testloginObject import TestLogPage
from iwebsns.config.conftest import login_path
from iwebsns.data.read_write import ReadWrite
from iwebsns.log.log import logger
import time

class Test_Creategroup:
    def test_1(self,test_logsystem):
        self.page1=TestLogPage(test_logsystem)
        file = ReadWrite(login_path)
        userlist = file.read()
        for user in userlist:
            self.page1.type_login_email(user[0])
            self.page1.type_login_pws(user[1])
            self.page1.click_loginsubm()
        self.page1.click_group()
        self.page1.click_creategroup()
        time.sleep(2)
        self.page1.type_groupname('沪上青玉流')
        self.page1.type_groupresume("人类高质量男性群")
        self.page1.type_grouptag('我的很大，你忍一下')
        self.page1.select_grouptype()
        self.page1.click_UploadButton()
        time.sleep(2)
        try:
            assert "沪上青玉流" in self.page1.check_creategroup
            print("测试用例成功：成功创建群组")
        except AssertionError:
            print("测试用例失败：创建群组失败")
            logger.info("验证用户创建群组信息......")

    def test_2(self,test_logsystem):
        self.page1 = TestLogPage(test_logsystem)
        self.page1.click_creategroup()
        time.sleep(2)
        self.page1.type_groupname('沪上青玉流')
        self.page1.type_groupresume("人类高质量男性群")
        self.page1.type_grouptag('我的很大，你忍一下')
        self.page1.click_UploadButton()
        time.sleep(2)
        try:
            assert "请认真填写每个选项" in self.page1.test_creategroup
            print("测试用例成功：成功弹出对应信息")
        except AssertionError:
            print("测试用例失败：未弹出对应提示信息")
            logger.info("验证用户创建群组失败信息......")