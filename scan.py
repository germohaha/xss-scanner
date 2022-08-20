import requests
import time
from scrapy.spiders import Spider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import scrapy
from lxml import etree 
import bs4
from bs4 import BeautifulSoup
from colorama import Fore,Style
#packages


print(Fore.RED+ '''
//\\ .. //\\
//\((  ))/\\
/  < `' >  \
''')
website = input("URL?: -> ")
reset = Style.RESET_ALL
print(reset)
print("scanning...", website)
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
       print(response.website)
#a class which holds variables
    #a function which parses and gets the response 


variable = requests.get(website).elapsed.total_seconds()
resp = requests.get(payload)
#sends a requests to website with payload attached
code = resp.status_code
#status code
soup = BeautifulSoup(resp.content,'lxml')
#parses the response content 

print(variable,"response time")
#tells you the response time
time.sleep(1)


if resp.status_code == 200:
  print('success! its valid')
else:
  print("failure")

print(reset)
input = input("do you want to return the web page code src?: ")
if input == "yes":
  r = requests.get(website)
  print("getting info...")
  
  time.sleep(1)
  
  print("getting info..")
  
  time.sleep(1)
  
  soup = bs4.BeautifulSoup(r.text, "html.parser")
  print(soup)
  #parses html content then prints it if input = yes
else:
  print("goodbye!")


