"""
    MUST HAVE CHROME DRIVER LOCATED IN THE SAME FOLDER AS THIS FILE ALONG WITH SELENIUM
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://olx.com.pk")

search_bar = driver.find_element(By.CSS_SELECTOR, "._1dc43551 ._162767a9")

search_bar.send_keys("Mobile Phones" + Keys.ENTER) # test search

# scrolls a 5 times down
for i in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "_95dae89d")))
    load_more = driver.find_element(By.CLASS_NAME, "_95dae89d") # check navigation
    load_more.click()
    time.sleep(2)

logo = driver.find_element(By.CLASS_NAME, "b28a1eb6") # check home button (logo)
logo.click() # does not start at top of page

time.sleep(5)
driver.execute_script("window.scrollTo(0, 0);")

categories = driver.find_element(By.CLASS_NAME, "f4cbb336") # check categories
categories.click()

time.sleep(2)
categories.click()

driver.find_element(By.CSS_SELECTOR, 'button[onclick^="moeRemoveBanner()"').click() # check popup rejection
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "._0089035e").click()

time.sleep(2)
driver.execute_script("document.querySelector('.ab5c51c3').scrollTop=300;") # to scroll dropdown
time.sleep(2)

WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "_4b2c6986")))
driver.find_elements(By.CLASS_NAME, "_4b2c6986")[3].click() # check location filter
driver.execute_script("window.scrollTo(0, 0);")

time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(10)