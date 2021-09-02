import pytest
from selenium import webdriver
from iwebsns.config.conftest import url,driver_path


@pytest.fixture(scope='module')
def test_logsystem(request):
    browser = webdriver.Firefox(executable_path=driver_path)
    browser.get(url)
    browser.maximize_window()
    browser.implicitly_wait(10)  # 隐形等待
    yield browser
    browser.quit()


