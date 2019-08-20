from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
import os

url = 'https://venmo.com'

chromedriverName = 'chromedriver'
PROJECT_ROOT = os.getcwd()
DRIVER_BIN = os.path.join(PROJECT_ROOT, chromedriverName)
driver = webdriver.Chrome(executable_path = DRIVER_BIN)
driver.get(url)

command_executor = driver.command_executor._url
session_id = driver.session_id

f = open('session_info.txt', 'w')
f.write(command_executor)
f.write('\n')
f.write(session_id)
f.close()

foo = input()
