from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import webbrowser
# import openpyxl
import requests
import bs4
from bs4 import BeautifulSoup
import re
import lxml
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.item import Item, Field

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

        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
        # element = i.get_attribute('href')
        driver.get(i.get_attribute('href'))
        driver.implicitly_wait(10)
        if len(driver.find_elements_by_css_selector("*[class*='phoneShowNumberButton']")) > 0:
            linkElem =driver.find_element_by_css_selector("*[class*='phoneShowNumberButton']")
            type(linkElem)
            linkElem.click()
            driver.implicitly_wait(5)
            print linkElem.text

        def parse(self, response):
            """
            The lines below is a spider contract. For more info see:
            http://doc.scrapy.org/en/latest/topics/contracts.html
            @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
            @scrapes name
            """
            sel = Selector(response)
            sites = sel.xpath('//ul[@class="directory-url"]/li')
            items = []
            r = requests.get(driver.current_url)  # where url is the above url
            bs = BeautifulSoup(r.text, 'lxml')

            for site in sites:
                item = bs()
                item['name'] = site.xpath('a/text()').extract()
                item['url'] = site.xpath('a/@href').extract()
                item['description'] = site.xpath('text()').re('-\s[^\n]*\\r')
                items.append(item)

                print items
                return items

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
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
        driver.implicitly_wait(5)
        print i.get_attribute('href')

driver.quit()