from iwebsns.testpageobjects.testloginObject import TestLogPage
from iwebsns.config.conftest import login_path
from iwebsns.data.read_write import ReadWrite
from iwebsns.log.log import logger
import time

class Test_InputPhoto:
    def test_1(self,test_logsystem):
        self.page1=TestLogPage(test_logsystem)
        file = ReadWrite(login_path)
        userlist = file.read()
        for user in userlist:
            self.page1.type_login_email(user[0])
            self.page1.type_login_pws(user[1])
            self.page1.click_loginsubm()
        self.page1.click_photoalbum()
        time.sleep(1)
        self.page1.click_inputphoto()
        time.sleep(2)
        self.page1.select_album()
        time.sleep(2)
        self.page1.input_photo("C:\\Users\\吾之梦\\Desktop\\QQ图片20210816110236.png")
        time.sleep(2)
        self.page1.click_updata()
        try:
            self.page1.click_myphoto()
            assert '共1张图片' in self.page1.check_myphoto
            print("测试用例成功：上传相片成功")
        except AssertionError:
            print("测试用例失败：上传相片失败")
            logger.info("验证用户成功上传相片信息......")

    def test_2(self,test_logsystem):
        self.page1=TestLogPage(test_logsystem)
        self.page1.click_inputphoto()
        time.sleep(2)
        self.page1.select_album()
        time.sleep(2)
        self.page1.input_photo("C:\\Users\\吾之梦\\Desktop\\QQ图片20210816110236.png")
        time.sleep(2)
        self.page1.click_updata()
        try:
            self.page1.click_myphoto()
            assert '重复的照片不能上传' in self.page1.check_myphoto
            print("测试用例成功：成功弹出提示")
        except AssertionError:
            print("测试用例失败：成功上传照片")
            logger.info("验证用户上传相片失败弹出弹窗信息......")




