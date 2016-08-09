from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import webbrowser
# import openpyxl
import requests
from io import StringIO, BytesIO
import bs4
from bs4 import BeautifulSoup
import re
import codecs
import lxml
import lxml.html
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.item import Item, Field
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from Kijiji_Scraper_Selenium import items
from scrapy.selector import Selector
from lxml.html import fromstring
from scrapy.http import HtmlResponse
from lxml.html.soupparser import fromstring
from lxml import etree
from xml.etree.cElementTree import tostring
from cssselect import GenericTranslator
from lxml.etree import XPath
from lxml.cssselect import CSSSelector
import os
import lxml.html as html # pip install 'lxml>=2.3.1'
from lxml.html.clean        import Cleaner
from selenium.webdriver     import Firefox         # pip install selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import xlsxwriter
import sys


reload(sys)
sys.setdefaultencoding('utf-8')

driver = webdriver.Firefox()
driver.get('http://www.kijiji.com')
# driver.implicitly_wait(10)
try:
    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "SignInLink"))
    )
finally:
    linkElem = driver.find_element_by_id('SignInLink')
    type(linkElem)
    linkElem.click() # follows the "Read It Online" link

try:
    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "LoginEmailOrNickname"))
    )
finally:
    emailElem = driver.find_element_by_id('LoginEmailOrNickname')
    emailElem.send_keys('williamleonardjohnson@gmail.com')
    passwordElem =driver.find_element_by_id('login-password')
    passwordElem.send_keys('WJ1029vc1')
    passwordElem.submit()

# emailElem =driver.find_element_by_id('LoginEmailOrNickname')
# emailElem.send_keys('williamleonardjohnson@gmail.com')
# passwordElem =driver.find_element_by_id('login-password')
# passwordElem.send_keys('WJ1029vc1')
# passwordElem.submit()
# driver.implicitly_wait(10)

try:
    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "houses for sale"))
    )
finally:
    linkElem = driver.find_element_by_partial_link_text("houses for sale")
    type(linkElem)
    linkElem.click()  # follows the "Read It Online" link

# linkElem =driver.find_element_by_partial_link_text("houses for sale")
# type(linkElem)
# linkElem.click()
# driver.implicitly_wait(3)

try:
    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Propri"))
    )
finally:
    linkElem = driver.find_element_by_partial_link_text("Propri")
    type(linkElem)
    linkElem.click()  # follows the "Read It Online" link

# linkElem =driver.find_element_by_partial_link_text("Propri")
# type(linkElem)
# linkElem.click()

try:
    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, "titlecount")))
finally:
    linkcount_label = driver.find_element_by_class_name("titlecount")
    titlecount_text = linkcount_label.get_attribute('textContent')

adnumber = 0
title_count = re.sub("[^0-9.]", "", titlecount_text)
title_count= int(title_count)
s=title_count/20
# helloFile = open('houses.txt', 'a')
xbook = xlsxwriter.Workbook('Test.xlsx')
xsheet = xbook.add_worksheet('Test')
outputFile = open('output.csv', 'a')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['label1', 'label2', 'label3', 'label4', 'label5', 'label6', 'label7', 'label8', 'label9', 'label10'])

for a in range(s):

    driver.get(driver.current_url)
    list_links = driver.find_elements_by_css_selector("*[class^='title enable-search-navigation-flag']")
    list_links1 = []
    for i1 in list_links:
        list_links1.append(i1.get_attribute('href'))

    b = 0

    for i in list_links:

        #Open a new tab and open individual kijiji ad

        print list_links1[b]

        if b == 0:
            try:
                element = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.TAG_NAME, "body")))
            finally:
                driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')

        # element = i.get_attribute('href')
        driver.get(list_links1[b])

        texts = []


        if len(driver.find_elements_by_css_selector("*[class*='phoneShowNumberButton']")) > 0:
            linkElem = driver.find_element_by_css_selector("*[class*='phoneShowNumberButton']")
            type(linkElem)
            linkElem.click()
            driver.implicitly_wait(5)
            phone_num=linkElem.text
            print linkElem.text

        if 'phone_num' in locals():
            texts.append(phone_num)
        else:
            texts.append(',')

        try:
            element = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[class='ad-attributes']")))
        finally:
            info = driver.find_element_by_css_selector("[class='ad-attributes']")

        # info = driver.find_element_by_css_selector("[class='ad-attributes']") was replaced by 161 to 165
        description = driver.find_element_by_id("AdDescriptionTabs")
        getinfo = info.find_elements_by_tag_name("td")
        for a in getinfo:
            texts.append(a.get_attribute('textContent'))
        # print texts
        # print description.get_attribute('textContent')
        home_desc = description.get_attribute('textContent')

        texts.append(home_desc)
        texts1 = texts

        str1='|'.join(texts)

        str1 = re.sub(r'\s+', ' ', str1.replace(' |', ' |'))
        # str1 = str1.strip('\n')
        texts = str1.split('|')

        outputWriter.writerow([str1])

        if adnumber <= title_count:
            xsheet.write_row(adnumber, 0, texts)
            adnumber += 1


        # texts.append(phone_num)
        # texts.append(home_desc)
        # with codecs.open('houses.txt', "a", 'utf-8') as text_file:
        #     if 'phone_num' in locals():
        #         text_file.write(phone_num.encode("utf-8"))
        #     text_file.write(',\n')
        #     str1=','.join(texts)
        #     text_file.write(str1.encode("utf-8"))
        #     text_file.write(',\n')
        #     text_file.write(home_desc)
        #     text_file.write(',\n')

        if 'phone_num' in locals():
            del phone_num

        b += 1

    try:
        element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.TAG_NAME, "body")
                                           ))
    finally:
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')

    try:
        element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Suivante")
                                           ))
    finally:
        linkElem=driver.find_element_by_partial_link_text("Suivante")
        type(linkElem)
        linkElem.click()

xbook.close()
driver.quit()