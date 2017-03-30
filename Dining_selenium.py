# install chromedriver and python packages
import time
import os
from selenium import webdriver

url = 'https://disneyworld.disney.go.com/dining/'
driver_path = 'C:/Program Files (x86)/Google/Chrome/chromedriver.exe'
if not os.path.exists('output'):
	os.makedirs('output')
	
driver = webdriver.Chrome(driver_path)
driver.get(url)
time.sleep(5)

# write entire content to file
with open('./output/dining.txt', 'w') as f:
    f.write(driver.page_source.encode('utf-8'))

# write useful fields into csv
# 357 restaurants
string = ''
for i in range(1, 358):
    restaurant = driver.find_element_by_xpath('//*[@id="alpha-default"]/li[{}]'.format(i))
    id = restaurant.get_attribute("data-entityid").split(';')[0]
    temp = restaurant.text.split('\n')
    string += '"'
    string += id
    string += '","'
    string += temp[0]
    string += '","'
    string += temp[3]
    string += '"\n'


with open('./output/dining.csv', 'w') as f:
    f.write(string.encode('utf-8'))

driver.close()