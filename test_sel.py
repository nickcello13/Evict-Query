from selenium import webdriver
import requests
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()


base_url = "https://eaccess.dccourts.gov/eaccess/home.page.2"
# go to the google home page
driver.get(base_url)
captcha_element = driver.find_element_by_id("captchaImg")
src_img_url = captcha_element.get_property("src")


# the page is ajaxy so the title is originally this:
# print(driver.title)

requests.get(base_url + src_img_url)

