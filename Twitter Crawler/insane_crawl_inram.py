from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from lxml import etree
import datetime


#start_date=input("Give starting date:")
#end_date=input("Give end date:")
#start_date=datetime.datetime.strptime(start_date,'%Y-%m-%d')
#end_date=datetime.datetime.strptime(end_date,'%Y-%m-%d')

#def inram():
url=urlopen("https://www.instagram.com/people")
html=url.read()
soup=BeautifulSoup(html,"html.parser")
elem=soup.find('img',{'id':'pImage_0'})
print((elem))
url.close()
#inram()