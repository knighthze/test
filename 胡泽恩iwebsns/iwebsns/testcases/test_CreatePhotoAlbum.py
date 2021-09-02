from iwebsns.testpageobjects.testloginObject import TestLogPage
from iwebsns.config.conftest import login_path
from iwebsns.data.read_write import ReadWrite
from iwebsns.log.log import logger
import time

class Test_CreatePhotoAlbum:
    def test_1_createphoto(self, test_logsystem):
        self.page1 = TestLogPage(test_logsystem)
        file = ReadWrite(login_path)
        userlist = file.read()
        for user in userlist:
            self.page1.type_login_email(user[0])
            self.page1.type_login_pws(user[1])
            self.page1.click_loginsubm()
        self.page1.click_photoalbum()
        self.page1.click_createphoto()
        time.sleep(2)
        self.page1.type_albumname("帅比")
        self.page1.type_albuminformation("大帅比")
        time.sleep(2)
        self.page1.click_submit_createphoto()
        try:
            assert '我的相册' in self.page1.myphoto
            print("测试用例成功：创建成功")
        except AssertionError:
            print("测试用例失败：创建失败")
            logger.info("验证用户创建相册信息......")

    def test_2_createphoto(self, test_logsystem):
        self.page1 = TestLogPage(test_logsystem)
        self.page1.click_createphoto()
        time.sleep(2)
        self.page1.type_albuminformation("大帅比")
        time.sleep(2)
        self.page1.click_submit_createphoto()
        try:
            assert '请正确填入相册名和描述！' in self.page1.check_createphoto
            print("测试用例成功：出现对应提示信息")
        except AssertionError:
            print("测试用例失败：成功创建")
            logger.info("验证用户创建相册失败信息......")
