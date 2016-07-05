# coding=utf-8

import requests
from bs4 import BeautifulSoup
import sys
from pymongo import MongoClient
client = MongoClient('127.0.0.1', 27017)
db = client.house_database



reload(sys)
sys.setdefaultencoding('utf-8')


def detailgjscrapy(url):
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
    result = requests.get(url,headers = headers)
    soup = BeautifulSoup(result.text,"lxml")
    title = soup.find("h3",class_="fl").text  # 标题
    #房源信息
    houseInfo_01  = soup.find_all("dl",class_="p_phrase cf")
    rentPrice = houseInfo_01[0].find("span",class_="f26").text
    rentAdvance = houseInfo_01[1].find("dd").text
    houseType = houseInfo_01[2].find("dd").text
    rentType = houseInfo_01[3].find("dd").text
    name = houseInfo_01[4].find("dd").find('a').text
    position_array = houseInfo_01[5].find("dd").find_all('a')
    position = ""
    for item in position_array:
        position += item.text

    renovation = houseInfo_01[6].find("dd").text
    area = houseInfo_01[7].find("dd").text
    orientation = houseInfo_01[8].find("dd").text
    floor = houseInfo_01[9].find("dd").text
    houseType_01 = houseInfo_01[10].find("dd").text

    furniture_list = soup.find("div",id="proLinks").find_all("span")
    furniture = ""
    for item_f in furniture_list:
         furniture += (item_f.text+",")
    describe =  soup.find("div",id="propContent").text
    otherInfo=  soup.find("div",class_="text-mute extra-info").text
    infoArr = otherInfo.split("，");
    num = infoArr[0].split("：")[1];
    creatAt = infoArr[1].split("：")[1];
    # 小区信息

    address = houseInfo_01[13].find("dd").text
    developer = houseInfo_01[14].find("dd").text
    propertyCompany = houseInfo_01[14].find("dd").text

    insideImgList = soup.find("div",class_="picCon").find_all("li");

    imglist=[];
    for item_img in insideImgList:
        imglist.append(item_img.img['src'])

    posts ={
        "title" : title,
        "num" : num,
        "creatAt" : creatAt,
        "houseCategoty" : 3,   # 3租房
        "houseInfo":{
            "rentPrice":rentPrice,
            "rentType":rentType,
            "furniture":furniture,
            "area":area,
            "orientation":orientation,
            "renovation":renovation,
            "floor":floor,
            "houseType_01":houseType_01,
            "furniture":furniture,
            "describe":describe,
            "insideImg":imglist
        },
        "villageInfo":{
            "name":name,
            "address":address,
            "developer":developer,
            "propertyCompany":propertyCompany


        }
    }
    print db.posts.insert_one(posts)
    #print soup
