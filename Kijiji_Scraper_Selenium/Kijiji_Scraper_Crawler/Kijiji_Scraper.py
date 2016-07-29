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
driver.get(driver.current_url)
list_links = driver.find_elements_by_css_selector("*[class^='title enable-search-navigation-flag']")

for i in list_links:

#Open a new tab and open individual kijiji ad

        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
        # element = i.get_attribute('href')
        driver.get(i.get_attribute('href'))
        if len(driver.find_elements_by_css_selector("*[class*='phoneShowNumberButton']")) > 0:
            linkElem = driver.find_element_by_css_selector("*[class*='phoneShowNumberButton']")
            type(linkElem)
            linkElem.click()
            driver.implicitly_wait(5)
            print linkElem.text

        
        html_string1 = requests.get(driver.current_url)
        print html_string1.pag
        sel = CSSSelector(html_string1.content)
        # parser = etree.XMLParser(ns_clean=True)
        text1=sel.text
        tree = lxml.html.document_fromstring(text1)
        # root = etree.fromstring(tree)
        print lxml.html.tostring(tree)

        # print nmetree.tostring(tree.getroot())
        Selector(text=content).xpath('//tbody/text()').extract()
        driver.implicitly_wait(10)
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
        driver.implicitly_wait(5)
        print i.get_attribute('href')
    #Check if there is a phone number and click on the show phone number and print phone number


# #To find and extract other parts of kijiji house ad
#         class KijijiAptmntSpider(CrawlSpider):
#                 name = "kijiji_aptmnt_spider"
#                 allowed_domains = ["kijiji.ca"]
#                 start_urls = ["http://www.kijiji.ca/b-apartments-condos/ottawa/c37l1700185"]
#                 rules = [
#                     Rule(
#                         LinkExtractor(
#                             allow=["http://www.kijiji.ca/v-\d-bedroom-apartments-condos/ottawa/.+"]
#                         ),
#                         callback='parse_item'),
#                     Rule(
#                         LinkExtractor(
#                             allow=["http://www.kijiji.ca/b-apartments-condos/ottawa/.*?/page-[0-5]/.+"]
#                         )
#                     )
#                 ]
#
#
# def parse_item(self, response):
#
#     aptmnt = items.AptmntItem()
#
#     aptmnt["url"] = response.url
#     aptmnt["address"] = self._extract_field(response, "Address")
#     aptmnt["price"] = self._extract_field(response, "Price")
#     aptmnt["date_listed"] = self._extract_field(response, "Date Listed")
#     aptmnt["num_bathrooms"] = self._extract_field(response, "Bathrooms (#)")
#     aptmnt["num_bedrooms"] = self._extract_bedrooms(response)
#     aptmnt["title"] = self._extract_title(response)
#     aptmnt["description"] = self._extract_description(response)
#
#     return aptmnt
#
#
#                 def _clean_string(self, string):
#                     for i in [",", "\n", "\r", ";", "\\"]:
#                         string = string.replace(i, "")
#                     return string.strip()
#
#
#                 def _extract_title(self, response):
#                     l = " ".join(response.xpath("//h1/text()").extract())
#                     return self._clean_string(l)
#
#
#                 def _extract_description(self, response):
#                     l = " ".join(response.xpath("//span[@itemprop='description']/text()").extract())
#                     return self._clean_string(l)
#
#
#                 def _extract_field(self, response, fieldname):
#                     l = response.xpath("//th[contains(text(), '{0}')]/following::td[1]//./text()".
#                                        format(fieldname)).extract()
#                     return l[0].strip() if l else None
#
#
#                 def _extract_bedrooms(self, response):
#                     r = re.search(r'kijiji.ca\/v-(\d)-bedroom-apartments-condos', response.url)
#                     return r.group(1).strip() if r else None

            # info = bs.select('table.ad-attributes > tbody')
        # print bs
        # for home in bs.findAll('div','layout-2 under-960-width-col-2-above clearfix allow-overflow', "html.parser"):
        #     html_string = requests.get(driver.current_url)
        #     soup = BeautifulSoup(html_string, "html.parser")
        # phone_num = re.search('AdIdZ(\d+)',bs)
        # phone_num = bs.find(text=re.compile('a.profileLink__legacy--jss(.*)'))
        # phone_num = bs.find('a', attrs={"class": re.compile(r"a.profileLink__legacy--jss" )})
        # phone_num = list_links = driver.find_element_by_css_selector("*[class^='profileLink__legacy--jss']")

        # phone_num = re.findall(r'^(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?$')
        # phone_num = bs.find('a', text = re.compile('a.profileLink__legacy--jss(.*)'), attrs = {'class' : 'pos'})

        # genres = home.find('span','genre').findAll('a')
        # genres = [g.contents[0] for g in genres]
        # runtime = home.find('span','runtime').contents[0]
        # year = home.find('span','year_type').contents[0]
        # print phone_num, genres,runtime, rating, year


driver.quit()