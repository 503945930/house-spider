# coding=utf-8

import requests
from bs4 import BeautifulSoup
import re
import ajkdetailspider
def gjscrapy():
    url = "http://cd.zu.anjuke.com/"
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
    result = requests.get(url,params={'kw':'师大现代花园'},headers = headers)
    soup = BeautifulSoup(result.text,"lxml")
    result_div = soup.find_all("div",class_=re.compile("zu-itemmod"))
    print result_div[0].a['href']
    # ajkdetailspider.detailgjscrapy(result_div[0].a['href'])
  # print result_div
    for item in result_div:
        #　print item.a['href']
        # print item.div['link']
        ajkdetailspider.detailgjscrapy(item.a['href'])


if __name__ == '__main__':
    gjscrapy();