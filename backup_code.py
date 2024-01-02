import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

ser_obj= Service(r"C:\Users\RAM\Desktop\Facebook\driver\chromedriver.exe")
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome(service=ser_obj, options=chrome_options)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.facebook.com/")


def login():
    driver.find_element(By.ID, "email").send_keys("***********")
    driver.find_element(By.ID, "pass").send_keys("***********")
    driver.find_element(By.NAME, "login").click()
    search_input = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Search Facebook"]')
    search_input.send_keys("Facebook")
    search_input.send_keys(Keys.ENTER)
    driver.find_element(By.CSS_SELECTOR, 'a[aria-label="Facebook, Verified account"]').click()
    driver.find_element(By.CSS_SELECTOR, 'div[aria-label="See Options"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//span[text()="Follow"]').click() #liking post

    time.sleep(5)




# def login():
#     driver.find_element(By.ID, "email").send_keys("ayushmanacker@gmail.com")
#     driver.find_element(By.ID, "pass").send_keys("#hacker1234.")
#     driver.find_element(By.NAME, "login").click()
#     search_input = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Search Facebook"]')
#     search_input.send_keys("Facebook")
#     search_input.send_keys(Keys.ENTER)
#     driver.find_element(By.CSS_SELECTOR, 'a[aria-label="Facebook, Verified account"]').click()
#     # driver.find_element(By.XPATH, '(//span[text()="Like"])[8]').click() #liking post
#     driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Filters"]').click()
#     time.sleep(2)
#     driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Go to:"]').click()
#     driver.find_element(By.XPATH, '(//span[text()="2022"])').click()
#     driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Done"][tabindex="0"]').click()
#


    time.sleep(5)



def logout():
    driver.find_element(By.XPATH, "//div[@class='x78zum5 x1n2onr6']").click()  # clicking on profile icon
    driver.find_element(By.CSS_SELECTOR, 'div[data-nocookies="true"]').click()  # clicking on logut button
    time.sleep(5)



if __name__ == "__main__":
    login()
    # logout()

