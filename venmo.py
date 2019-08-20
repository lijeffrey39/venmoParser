from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
import time

f = open('session_info.txt', 'r')
command_executor = f.readline().rstrip()
session_id = f.readline().rstrip()

driver = webdriver.Remote(command_executor = command_executor)
driver.session_id = session_id

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
