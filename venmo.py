from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
import time
import pandas as pd
import os

f = open('session_info.txt', 'r')
command_executor = f.readline().rstrip()
session_id = f.readline().rstrip()

driver = webdriver.Remote(command_executor = command_executor)
driver.session_id = session_id

# while (driver.find_element_by_class_name('moreButton').text == "More"):
# 	try:
# 		more = driver.find_element_by_class_name('moreButton')
# 		more.click()
# 		# time.sleep(2)
# 	except:
# 		print("still going")


transactions = driver.find_elements_by_class_name('p_ten_t')[::-1]

results = []
current_balance = 0

for transaction in transactions:
	elements = transaction.find_elements_by_tag_name('td')
	if (len(elements) == 3):
		info = elements[1].find_element_by_class_name('width350').text
		money_text = elements[2].find_element_by_tag_name('span').text
		amount = float(money_text[2:])
		sign = money_text[0]
		charge = info.split('\n')
		to_from = charge[0]
		user = ''
		if (sign == '+'):
			current_balance += amount
		else:
			current_balance -= amount

		results.append([to_from, sign, amount, current_balance])


# print(resul)

df = pd.DataFrame(results) 
current_path = os.getcwd()
df.to_csv(current_path + '.csv')
print("done")

foo = input()

print(driver.command_executor._url)
print(driver.session_id)

foo = input()
