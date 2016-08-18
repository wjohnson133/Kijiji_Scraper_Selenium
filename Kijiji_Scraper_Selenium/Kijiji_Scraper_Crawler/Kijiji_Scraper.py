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
import lxml.html as html  # pip install 'lxml>=2.3.1'
from lxml.html.clean import Cleaner
from selenium.webdriver import Firefox  # pip install selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
import csv
import xlsxwriter
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

new_driver = webdriver.PhantomJS()
driver = webdriver.PhantomJS()
# new_driver = webdriver.PhantomJS(
#     executable_path='/Users/williamjohnson/PycharmProjects/Kijiji_Scraper_Selenium/Kijiji_Scraper_Selenium/Kijiji_Scraper_Crawler/phantomjs')
# new_driver.set_window_size(1920, 1080)
# new_driver.maximize_window()
new_driver_handle = new_driver.current_window_handle
# driver = webdriver.PhantomJS(
#     executable_path='/Users/williamjohnson/PycharmProjects/Kijiji_Scraper_Selenium/Kijiji_Scraper_Selenium/Kijiji_Scraper_Crawler/phantomjs')
# driver.set_window_size(1920, 1080)
driver_handle = driver.current_window_handle
driver.get('http://www.kijiji.com')
# driver.implicitly_wait(10)
try:
    element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "SignInLink")))
finally:
    linkElem = driver.find_element_by_id('SignInLink')
    type(linkElem)
    linkElem.click()  # follows the "Read It Online" link

try:
    element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "LoginEmailOrNickname")))
finally:
    emailElem = driver.find_element_by_id('LoginEmailOrNickname')
    emailElem.send_keys('williamleonardjohnson@gmail.com')
    passwordElem = driver.find_element_by_id('login-password')
    passwordElem.send_keys('WJ1029vc1')
    passwordElem.submit()

# emailElem =driver.find_element_by_id('LoginEmailOrNickname')
# emailElem.send_keys('williamleonardjohnson@gmail.com')
# passwordElem =driver.find_element_by_id('login-password')
# passwordElem.send_keys('WJ1029vc1')
# passwordElem.submit()
# driver.implicitly_wait(10)

try:
    element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "houses for sale"))
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
    element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Propri")))
finally:
    linkElem = driver.find_element_by_partial_link_text("Propri")
    type(linkElem)
    linkElem.click()  # follows the "Read It Online" link

# linkElem =driver.find_element_by_partial_link_text("Propri")
# type(linkElem)
# linkElem.click()

try:
    element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "titlecount")))
finally:
    linkcount_label = driver.find_element_by_class_name("titlecount")
    titlecount_text = linkcount_label.get_attribute('textContent')

adnumber = 0
title_count = re.sub("[^0-9.]", "", titlecount_text)
title_count = int(title_count)
s = title_count / 20
# helloFile = open('houses.txt', 'a')
xbook = xlsxwriter.Workbook('Test.xlsx')
xsheet = xbook.add_worksheet('Test')
outputFile = open('output.csv', 'a')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(
    ['label1', 'label2', 'label3', 'label4', 'label5', 'label6', 'label7', 'label8', 'label9', 'label10'])

for a in range(s):

    driver.get(driver.current_url)
    list_links = driver.find_elements_by_css_selector("*[class^='title enable-search-navigation-flag']")
    list_links1 = []
    for i1 in list_links:
        list_links1.append(i1.get_attribute('href'))

    b = 0

    new_driver.switch_to.window(new_driver_handle)

    for i in list_links:

        # Open a new tab and open individual kijiji ad

        print list_links1[b]

        if b > 0:
            new_driver.get(list_links1[b])

        if adnumber == 0:
            new_driver.switch_to.window(new_driver_handle)
            new_driver.get(list_links1[b])
            try:
                element = WebDriverWait(new_driver, 30).until(
                    EC.presence_of_element_located((By.ID, "SignInLink"))
                )
            finally:
                linkElem = new_driver.find_element_by_id('SignInLink')
                type(linkElem)
                linkElem.click()  # follows the "Read It Online" link

            try:
                element = WebDriverWait(new_driver, 30).until(
                    EC.presence_of_element_located((By.ID, "LoginEmailOrNickname")))
            finally:
                emailElem = new_driver.find_element_by_id('LoginEmailOrNickname')
                emailElem.send_keys('williamleonardjohnson@gmail.com')
                passwordElem = new_driver.find_element_by_id('login-password')
                passwordElem.send_keys('WJ1029vc1')
                passwordElem.submit()

        new_driver.save_screenshot('out1.png')

        texts = []

        try:
            element = WebDriverWait(new_driver, 30).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "*[class*='phoneShowNumberButton']"))
            )
        except (NoSuchElementException, TimeoutException):
            pass
        else:
            linkElem = new_driver.find_element_by_css_selector("*[class*='phoneShowNumberButton']")
            type(linkElem)
            new_driver.implicitly_wait(2)
            # linkElem.click()

            while True:
                new_driver.implicitly_wait(2)
                try:
                    # len(linkElem.text) > 0
                    linkElem.click()
                    phone_num = linkElem.text
                    if re.search('XX', phone_num):
                        continue
                except (StaleElementReferenceException, TimeoutException):
                    continue
                else:
                    print linkElem.text
                    break

        # if len(new_driver.find_elements_by_css_selector("*[class*='phoneShowNumberButton']")) > 0:
        #     linkElem = new_driver.find_element_by_css_selector("*[class*='phoneShowNumberButton']")
        #     type(linkElem)
        #     linkElem.click()
        #     new_driver.implicitly_wait(5)
        #     phone_num = linkElem.text
        #     print linkElem.text

        if 'phone_num' in locals():
            texts.append(phone_num)
        else:
            texts.append(',')

        try:
            element = WebDriverWait(new_driver, 30).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "[class='ad-attributes']"))
            )
        except (NoSuchElementException, TimeoutException):
            continue
        else:
            info = new_driver.find_element_by_css_selector("[class='ad-attributes']")

        # info = driver.find_element_by_css_selector("[class='ad-attributes']") was replaced by 161 to 165
        description = new_driver.find_element_by_id("AdDescriptionTabs")
        getinfo = info.find_elements_by_tag_name("td")
        for a in getinfo:
            texts.append(a.get_attribute('textContent'))
        # print texts
        # print description.get_attribute('textContent')
        home_desc = description.get_attribute('textContent')

        texts.append(home_desc)
        texts1 = texts

        str1 = '|'.join(texts)

        str1 = re.sub(r'\s+', ' ', str1.replace(' |', ' |'))
        # str1 = str1.strip('\n')
        texts = str1.split('|')

        outputWriter.writerow([str1])

        if adnumber <= title_count:
            xsheet.write_row(adnumber, 0, texts)
            adnumber += 1

        if 'phone_num' in locals():
            del phone_num

        b += 1

    driver.switch_to.window(driver_handle)

    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Suivante"))
        )
    finally:
        linkElem = driver.find_element_by_partial_link_text("Suivante")
        type(linkElem)
        linkElem.click()

xbook.close()
driver.quit()
