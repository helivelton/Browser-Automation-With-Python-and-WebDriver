import os
from selenium import webdriver

#checking if shots folder exists and creating it otherwise
if not os.path.exists('shots'):
    os.makedirs('shots')

#reading the url_list.txt file and puting entries on a list
urls = []
with open('url_list.txt') as file_list:
    urls = file_list.readlines()

#defining path to webdriver and launch chrome browser
driver = webdriver.Chrome('bin/chromedriver')

count = 0
for url in urls:
    url = url.strip() #removing the newline character

    driver.get(url)
    driver.save_screenshot('shots/screenshot{}.png'.format(count))
    count = count + 1

driver.close()