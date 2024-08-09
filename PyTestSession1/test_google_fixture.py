from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

driver = None
@pytest.fixture(scope='module')
def init_driver():
    global driver
    print("-------------setup-------------")
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("http:\\www.google.com")

    yield
    print("-----------teardown---------")
    driver.quit()

@pytest.mark.usefixtures("init_driver")
def test_google_title():
    assert driver.title == "Google"

@pytest.mark.usefixtures("init_driver")
def test_url():
    assert driver.current_url =="https://www.google.com/"


#command for run:  pytest test_google_fixture.py -v -s --html=test_google_fixture_report.html
