from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


class TestLogPage:
    def __init__(self,driver):
        self.login_email=By.NAME,'login_email'
        self.login_pws=By.NAME,'login_pws'
        self.loginsubm=By.ID,'loginsubm'
        self.browser=driver
        self.logout=By.LINK_TEXT,'退出'
        self.log=By.PARTIAL_LINK_TEXT,"日志"
        self.createlog=By.PARTIAL_LINK_TEXT,"新建日志"
        self.blog_title=By.NAME,"blog_title"
        self.tag=By.NAME,"tag"
        self.ke_content=By.ID,"KINDEDITORIFRAME"
        self.submit_createlog = By.CSS_SELECTOR,'[onclick="javascript:is_submit=1;"]'
        self.test_createlog = By.PARTIAL_LINK_TEXT,"请填写标题"
        self.addclassification=By.PARTIAL_LINK_TEXT,"添加分类"
        self.new_sort_name=By.ID,"new_sort_name"
        self.save_sort_name=By.CSS_SELECTOR,'[value="保存"]'
        self.find_sort_name=By.ID,"blog_sort_list"
        self.logclass=By.PARTIAL_LINK_TEXT,"日志分类"
        self.check_logclass = By.PARTIAL_LINK_TEXT,"smart"
        self.back=By.PARTIAL_LINK_TEXT,"返回上一级"
        self.test_logclass = By.PARTIAL_LINK_TEXT,"请填写信息"
        self.check_back = By.CLASS_NAME,"app_blog"
        self.edit=By.PARTIAL_LINK_TEXT,"编辑"
        self.type_edit=By.CLASS_NAME,"small-text"
        self.save_type_edit=By.CSS_SELECTOR,'[value="保存"]'
        self.check_edit = By.PARTIAL_LINK_TEXT,"handsome"
        self.delete_class=By.PARTIAL_LINK_TEXT,"删除"
        self.photoalbum=By.PARTIAL_LINK_TEXT,"相册"
        self.createphoto=By.PARTIAL_LINK_TEXT,"新建相册"
        self.albumname=By.ID,"album_name"
        self.albuminformation=By.ID,"album_information"
        self.submit_createphoto=By.CSS_SELECTOR,'[value="创建"]'
        self.myphoto=By.PARTIAL_LINK_TEXT,'我的相册'
        self.check_createphoto=By.PARTIAL_LINK_TEXT,"请正确填入相册名和描述！"
        self.inputphoto=By.PARTIAL_LINK_TEXT,"上传相片"
        self.select_photoalbum=By.ID,"album_name"
        self.style_input=By.PARTIAL_LINK_TEXT,"切换上传方式"
        self.attach=By.ID,"attach[]"
        self.updata=By.CLASS_NAME,"regular-btn"
        self.check_myphoto=By.PARTIAL_LINK_TEXT,"共1张图片"
        self.group=By.PARTIAL_LINK_TEXT,"群组"
        self.creategroup=By.PARTIAL_LINK_TEXT,"创建群组"
        self.groupname=By.ID,"group_name"
        self.groupresume=By.ID,'group_resume'
        self.grouptag=By.ID,"tag"
        self.grouptype=By.ID,'group_type'
        self.uploadbutton=By.ID,'UploadButton'
        self.check_creategroup=By.PARTIAL_LINK_TEXT,'沪上青玉流'
        self.test_creategroup=By.PARTIAL_LINK_TEXT,'请认真填写每个选项'
        self.searchgroup=By.PARTIAL_LINK_TEXT,"搜索群组"
        self.search_groupname=By.ID,'group_name'
        self.search_submit=By.CSS_SELECTOR,'[value="查找"]'

    def type_login_email(self,login_email):
        self.browser.find_element(*self.login_email).send_keys(login_email)

    def type_login_pws(self,login_pws):
        self.browser.find_element(*self.login_pws).send_keys(login_pws)

    def click_loginsubm(self):
        self.browser.find_element(*self.loginsubm).click()

    def click_logout(self):
        self.browser.find_element(*self.logout).click()

    def click_log(self):
        self.browser.find_element(*self.log).click()

    def click_createlog(self):
        self.browser.switch_to.frame("frame_content")
        self.browser.find_element(*self.createlog).click()

    def type_blog_title(self,blog_title):
        self.browser.find_element(*self.blog_title).send_keys(blog_title)

    def type_tag(self,tag):
        self.browser.find_element(*self.tag).send_keys(tag)

    def type_ke_content(self,ke_content):
        self.browser.find_element(*self.ke_content).send_keys(ke_content)

    def click_submit_createlog(self):
        self.browser.switch_to.default_content()
        js = "var q=document.documentElement.scrollTop=10000"
        self.browser.execute_script(js)
        self.browser.switch_to.frame("frame_content")
        self.browser.find_element(*self.submit_createlog).click()

    def create_Duplicate_log(self):
        self.browser.switch_to.default_content()
        js = "var q=document.documentElement.scrollTop=-10000"
        self.browser.execute_script(js)
        self.browser.switch_to.frame("frame_content")
        self.browser.find_element(*self.createlog).click()

    def click_addclassification(self):
        self.browser.find_element(*self.addclassification).click()

    def type_new_sort_name(self,new_sort_name):
        self.browser.find_element(*self.new_sort_name).send_keys(new_sort_name)

    def click_save_sort_name(self):
        self.browser.find_element(*self.save_sort_name).click()

    def chose_sort_name(self):
        check = self.find_sort_name=By.ID,"blog_sort_list"
        Select(check).select_by_value("smart")
        time.sleep(1)

    def click_logclass(self):
        self.browser.find_element(*self.logclass).click()

    def Check_logclass(self):
        self.browser.find_element(*self.check_logclass).click()

    def click_back(self):
        self.browser.find_element(*self.back).click()

    def click_edit(self):
        self.browser.find_element(*self.edit).click()

    def Type_edit(self,Type_edit):
        self.browser.find_element(*self.type_edit).clear()
        self.browser.find_element(*self.type_edit).send_keys(Type_edit)

    def click_save_type_edit(self):
        self.browser.find_element(*self.save_type_edit).click()

    def click_delete_class(self):
        self.browser.find_element(*self.delete_class).click()

    def click_photoalbum(self):
        self.browser.find_element(*self.photoalbum).click()

    def click_createphoto(self):
        self.browser.switch_to.default_content()
        self.browser.switch_to.frame("frame_content")
        self.browser.find_element(*self.createphoto).click()

    def type_albumname(self,albumname):
        self.browser.find_element(*self.albumname).send_keys(albumname)

    def type_albuminformation(self,albuminformation):
        self.browser.find_element(*self.albuminformation).send_keys(albuminformation)

    def click_submit_createphoto(self):
        self.browser.find_element(*self.submit_createphoto).click()

    def click_inputphoto(self):
        self.browser.switch_to.default_content()
        self.browser.switch_to.frame("frame_content")
        self.browser.find_element(*self.inputphoto).click()

    def select_album(self):
        album=self.browser.find_element(*self.select_photoalbum)
        Select(album).select_by_visible_text("帅比")

    def input_photo(self,attach):
        self.browser.find_element(*self.style_input).click()
        self.browser.find_element(*self.attach).send_keys(attach)

    def click_updata(self):
        self.browser.find_element(*self.updata).click()

    def click_myphoto(self):
        self.browser.find_element(*self.myphoto).click()

    def click_group(self):
        self.browser.find_element(*self.group).click()

    def click_creategroup(self):
        self.browser.switch_to.default_content()
        self.browser.switch_to.frame("frame_content")
        self.browser.find_element(*self.creategroup).click()

    def type_groupname(self,groupname):
        self.browser.find_element(*self.groupname).send_keys(groupname)

    def type_groupresume(self,groupresume):
        self.browser.find_element(*self.groupresume).send_keys(groupresume)

    def type_grouptag(self,grouptag):
        self.browser.find_element(*self.grouptag).send_keys(grouptag)

    def select_grouptype(self):
        type=self.browser.find_element(*self.grouptype)
        Select(type).select_by_value('12')

    def click_UploadButton(self):
        self.browser.find_element(*self.uploadbutton).click()

    def click_searchgroup(self):
        self.browser.switch_to.default_content()
        self.browser.switch_to.frame("frame_content")
        self.browser.find_element(*self.searchgroup).click()

    def type_searchgroupname(self,groupname):
        self.browser.find_element(*self.search_groupname).send_keys(groupname)

    def click_searchsubmit(self):
        self.browser.find_element(*self.search_submit).click()








