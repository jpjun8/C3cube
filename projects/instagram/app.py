from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome('./chromedriver_win32/chromedriver.exe', chrome_options=chrome_options)
driver.get('https://instagram.com')

username = driver.find_element(By.NAME, 'username')
password = driver.find_element(By.NAME, 'password')
login = driver.find_element(By.CSS_SELECTOR, 'button._acan')

username.send_keys('joon.pyo.jun')
password.send_keys('Wkdgmlwls13!')
login.click()

time.sleep(5) # wait for the page to load

save_info = driver.find_element(By.CSS_SELECTOR, 'button._acan')
save_info.click()
