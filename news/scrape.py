import requests

from html.parser import HTMLParser

from bs4 import BeautifulSoup

import pprint

def parse_source():
        
    url = ("https://finviz.com/news.ashx?v=2")
    browser_headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    req = requests.get(url, headers=browser_headers)


    soup = BeautifulSoup(req.text, 'html.parser')



    urls = []
    for link in soup.find_all('a'):
        #print(link.get('href'))
        urls.append(link.get('href'))
        
    #print(urls)


    bloomberg = urls[20:30]
    reuters = urls[32:41]
    
    return bloomberg, reuters
#fox = urls[]

