from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

options = Options()
driver = webdriver.Firefox(options=options, executable_path=r'C:\driver\geckodriver.exe')
wait = WebDriverWait(driver, 10)
driver.get('https://login.yahoo.com')
driver.maximize_window()
sleep(5)
driver.find_element_by_xpath('//*[@id="login-username"]').send_keys('username')
sleep(5)
driver.find_element_by_xpath('//*[@id="login-username"]').send_keys(Keys.RETURN)
sleep(5)
driver.find_element_by_xpath('//*[@id="login-passwd"]').send_keys('password')
sleep(5)
wait.until(EC.presence_of_element_located((By.ID, 'login-passwd'))).send_keys(Keys.RETURN)
