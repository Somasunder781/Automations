from selenium import webdriver
import time

username = "accountname"
password = "accountpass"

# starts a new chrome session
chrome = webdriver.Chrome("C:\\python37\driver\chromedriver.exe")
time.sleep(1)

# maximize the window size
chrome.maximize_window()

# navigate to the url
chrome.get("https://www.instagram.com/")
time.sleep(4)

# finds the username box
usern = chrome.find_element_by_name("username")
# sends the entered username
usern.send_keys(username)

# finds the password box
passw = chrome.find_element_by_name("password")

# sends the entered password
passw.send_keys(password)

time.sleep(2)

# finds the login button
log_cl = chrome.find_element_by_xpath(
    "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div")
log_cl.click()  # clicks the login button
time.sleep(4)
