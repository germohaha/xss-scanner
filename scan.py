import requests
import time
from scrapy.spiders import Spider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import scrapy
from lxml import etree 
import bs4
from bs4 import BeautifulSoup
from colorama import Fore
#packages


print(Fore.RED+ '''
//\\ .. //\\
//\((  ))/\\
/  < `' >  \
''')
website = input("URL?: -> ")
payload = website + "<script>alert(1)</script>"
#variables
print("crawling...")
time.sleep(1)
print("crawling..")
class main(Spider):
  name = "spider"
  domains = website
  start = website
  def parse(self, response):
       self.logger.info('A response from %s just arrived!', response.url)
#a class and a function parsing and crawling the website variable value



variable = requests.get(website).elapsed.total_seconds()
resp = requests.get(payload)
code = resp.status_code
soup = BeautifulSoup(resp.content,'lxml')
#parses data

print(variable,"response time")
time.sleep(1)


if resp.status_code == 200:
  print('success! its valid')
else:
  print("failure")


input = input("do you want to return the web page code src?: ")
if input == "yes":
  r = requests.get(website)
  print("getting info...")
  
  time.sleep(1)
  
  print("getting info..")
  
  time.sleep(1)
  
  soup = bs4.BeautifulSoup(r.text, "html.parser")
  print(soup)
else:
  print("goodbye!")

