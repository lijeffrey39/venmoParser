from selenium import webdriver
import os
import time
from selenium.webdriver.remote.webdriver import WebDriver

# url = "https://venmo.com/lijeffrey39"

# chrome_options = webdriver.ChromeOptions()
# prefs = {"profile.managed_default_content_settings.images": 2}
# chrome_options.add_experimental_option("prefs", prefs)
# chrome_options.add_argument("--headless")
# chrome_options.add_argument('log-level=3')
# chromedriverName = 'chromedriver' if (platform.system() == "Darwin") else 'chromedriver.exe'
# PROJECT_ROOT = os.getcwd()
# DRIVER_BIN = os.path.join(PROJECT_ROOT, chromedriverName)

# driver = webdriver.Chrome(executable_path = DRIVER_BIN)
driver = webdriver.Remote(command_executor = 'http://127.0.0.1:49396')
driver.session_id = '794dfa49214193b476b3e4bc1e64d09a'
print(driver.current_url)

while (driver.find_element_by_class_name('moreButton').text == "More"):
	more = driver.find_element_by_class_name('moreButton')
	more.click()
	time.sleep(2)

allGreen = driver.find_elements_by_class_name('p_ten_t')
profit = 0

for g in allGreen:
	third = g.find_elements_by_tag_name('td')
	if (len(third) == 3):
		spanTd = third[2].find_element_by_tag_name('span').text
		print(spanTd)
		num = float(spanTd[2:])
		if (spanTd[0] == '-'):
			profit = profit - num
		else:
			profit = profit + num

print(profit)

foo = input()

print(driver.command_executor._url)
print(driver.session_id)

foo = input()
