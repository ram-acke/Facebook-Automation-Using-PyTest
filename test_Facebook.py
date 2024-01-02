import pytest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture(scope="module")
def launchBrowser():
    ser_obj = Service(r"C:\Users\RAM\Desktop\Facebook\driver\chromedriver.exe")
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    global driver
    driver = webdriver.Chrome(service=ser_obj, options=chrome_options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://www.facebook.com/")
    driver.implicitly_wait(10)
    yield
    driver.quit()

def test_Login(launchBrowser):
    driver.find_element(By.ID, "email").send_keys("*******************")
    driver.find_element(By.ID, "pass").send_keys("*****************")
    driver.find_element(By.NAME, "login").click()
    assert driver.current_url == "https://www.facebook.com/"


def test_Scrolling_Feed(launchBrowser):
    for i in range(10):
        driver.execute_script("window.scrollBy(0,1000)", "")
        time.sleep(2)


def test_SearchFriend_and_Scrolling_Posts(launchBrowser):
    search_input = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Search Facebook"]')
    search_input.send_keys("Facebook")
    search_input.send_keys(Keys.ENTER)
    driver.find_element(By.CSS_SELECTOR, 'a[aria-label="Facebook, Verified account"]').click()
    check = driver.find_element(By.CSS_SELECTOR ,'.xh8yej3 [aria-label="Message"]')
    if check.is_displayed():
        print("Profile Open")
    else:
        print("Profile Not Open")
    for i in range(1, 8):
        driver.execute_script("window.scrollBy(0,1000)", "")
        time.sleep(2)


