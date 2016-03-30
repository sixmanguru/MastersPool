from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

import time, re

import requests



dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36"
	)

driver = webdriver.PhantomJS(desired_capabilities=dcap)

driver.set_window_size(1024,768)

url = 'http://www.masters.com/en_US/scores/feeds/scores.json'

for i in range(5):
	time.sleep(10)
	driver.get(url)
	data = driver.page_source

	print data

