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
from werkzeug.contrib.cache import FileSystemCache # pip install werkzeug

driver = webdriver.Firefox()
driver.get('http://www.kijiji.com')
driver.implicitly_wait(10)
linkElem = driver.find_element_by_id('SignInLink')
type(linkElem)
linkElem.click() # follows the "Read It Online" link
driver.implicitly_wait(10)
emailElem =driver.find_element_by_id('LoginEmailOrNickname')
emailElem.send_keys('williamleonardjohnson@gmail.com')
passwordElem =driver.find_element_by_id('login-password')
passwordElem.send_keys('WJ1029vc1')
passwordElem.submit()
driver.implicitly_wait(10)
linkElem =driver.find_element_by_partial_link_text("houses for sale")
type(linkElem)
linkElem.click()
driver.implicitly_wait(3)
linkElem =driver.find_element_by_partial_link_text("Propri")
type(linkElem)
linkElem.click()

linkcount_label = driver.find_element_by_class_name("titlecount")
titlecount_text = linkcount_label.get_attribute('textContent')
title_count = re.sub("[^0-9.]", "", titlecount_text)
title_count= int(title_count)
s=title_count/20
helloFile = open('houses.txt', 'a')

for a in range(s):

    driver.get(driver.current_url)
    list_links = driver.find_elements_by_css_selector("*[class^='title enable-search-navigation-flag']")

    for i in list_links:

    #Open a new tab and open individual kijiji ad

        driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
        # element = i.get_attribute('href')
        driver.get(i.get_attribute('href'))
        if len(driver.find_elements_by_css_selector("*[class*='phoneShowNumberButton']")) > 0:
            linkElem = driver.find_element_by_css_selector("*[class*='phoneShowNumberButton']")
            type(linkElem)
            linkElem.click()
            driver.implicitly_wait(5)
            print linkElem.text


        texts = []
        info = driver.find_element_by_css_selector("[class='ad-attributes']")
        description = driver.find_element_by_id("AdDescriptionTabs")
        getinfo = info.find_elements_by_tag_name("td")
        for a in getinfo:
            texts.append(a.get_attribute('textContent'))
        print texts
        print description.get_attribute('textContent')
        phone_num = linkElem.text
        home_desc = description.get_attribute('textContent')
        # texts.append(phone_num)
        # texts.append(home_desc)
        helloFile.write(phone_num) f
        helloFile.write(',\n')
        str1=','.join(texts)
        str1 = str1.encode('utf-8')
        helloFile.write(str1, encoding='utf-8', xml_declaration=True)
        helloFile.write(',\n')
        helloFile.write(home_desc)
        helloFile.write(',\n')
        driver.implicitly_wait(10)
        driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')
        driver.implicitly_wait(5)
        print i.get_attribute('href')

    linkElem=driver.find_element_by_link_text('Suivante')
    type(linkElem)
    linkElem.click()

helloFile.close()
driver.quit()