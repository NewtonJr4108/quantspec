import lxml.html

import requests

url = 'https://finance.yahoo.com/gainers'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'}

def printStocks(url):
    ytext = requests.get(url,headers=headers).text
    yroot = lxml.html.fromstring(ytext)
    for x in yroot.xpath('//*[@id="fin-scr-res-table"]//a'):
        print(x.attrib['href'].split("/")[-1].split("?")[0])

printStocks(url)