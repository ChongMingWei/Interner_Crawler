#!/usr/bin/python
#coding:utf-8

from bs4 import BeautifulSoup
from urllib.request import urlopen
#from urllib2 import urlopen   #This is for python2
import re

html = urlopen("https://tw.appledaily.com/new/realtime").read().decode('utf-8')


soup = BeautifulSoup(html, features = 'lxml')
content = soup.find('li',{"class":"rtddt"})
c_content = content.find_all('a')
url = [l['href'] for l in c_content]
print(url[0])

newshtml = urlopen(url[0]).read().decode('utf-8')
soup2 = BeautifulSoup(newshtml, features = 'lxml')
title = re.findall(r"<h1>(.+?)</h1>",newshtml)
article = re.findall(r"<p>(.+?)</p>",newshtml,flags=re.DOTALL)#不同類型的新聞，包內容的前後標籤不一樣:


#title = soup2.find_all('h1')
new_article = []
temp_article = article[0]
print("標題:\n")
print(title[0]+"\n")
print("內容:\n")
print(article[0]+"\n")
output = re.sub('<.*?>','',temp_article)
output = re.sub('&nbsp','',output)
print("修改後內容:\n")	
print(output)

