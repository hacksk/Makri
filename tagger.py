#!/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import codecs


# URL = "http://www.iiitmk.ac.in/MalayalamPOSTagger/"
# driver = webdriver.Chrome("/usr/bin/chromedriver_linux64/chromedriver")
dirList = [x[0] for x in os.walk("./Data")]    
dirList = dirList[1:]

for domains in dirList:
	for files in os.listdir(domains):
		print(files)
		file = codecs.open(domains+"/"+files,encoding='utf-8')
		print(file)

driver.get(URL)
assert "Malayalam" in driver.title

textArea = driver.find_element_by_id("mal_text")
textArea.clear()
textArea.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source