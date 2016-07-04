# coding=utf-8

import requests
from bs4 import BeautifulSoup
import re
def gjscrapy():
    url = "http://chengdu.anjuke.com/sale/p2-rd1"
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
    result = requests.get(url,params={'from':'zjsr','kw':'东立国际花城'},headers = headers)
    soup = BeautifulSoup(result.text,"lxml")
    print soup.find_all("li",class_=re.compile("list"))


if __name__ == '__main__':
    gjscrapy();