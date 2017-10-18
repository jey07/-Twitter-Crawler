from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os.path 
import datetime
import codecs
import time


dayDelta = datetime.timedelta(days=2)
def crawl_daterange(startdate,enddate):
    start_date=startdate-datetime.timedelta(days=1)
    end_date=enddate-datetime.timedelta(days=1)
    foldername="Twitter_crawl_" +str(start_date)+"_to_"+str(end_date)
    path=os.getcwd()+"\\"+foldername+"\\"

    if not os.path.exists(path):
        os.makedirs(path)

    while startdate < enddate:
        driver=webdriver.Chrome(executable_path=r"C:/Python34/chromedriver.exe")
        try:
            driver.get("https://twitter.com/search-home")
            elem=driver.find_element_by_id("search-home-input")
            elem.clear()

            todate=start_date+dayDelta
            if(todate>enddate):
                todate=enddate
            
            print("Page crawling started for StartDate:"+ str(start_date)+" EndDate:"+str(todate))  

            elem.send_keys("from:people since:"+str(startdate)+ " until:"+str(todate))
            elem.send_keys(Keys.RETURN)
        except:
            driver.close()  

        html_source = driver.page_source
        old_page=html_source
        new_page = ""
        n = 50

        while(old_page!=new_page):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(4)
            old_page=new_page
            new_page=driver.page_source
            n=n-1
            if(n<0):
                break

        with codecs.open(path+str(startdate)+".html",mode="w",encoding="utf-8") as fp:
            fp.write(driver.page_source)

        start_date=startdate-datetime.timedelta(days=1)            
        startdate += dayDelta
        driver.close()  

start_date=input("Give start date in 'yyyy-mm-dd' format:")
end_date=input("Give end date in 'yyyy-mm-dd'format:")
start_date=datetime.datetime.strptime(start_date,'%Y-%m-%d').date()+datetime.timedelta(days=1)
end_date=datetime.datetime.strptime(end_date,'%Y-%m-%d').date()+datetime.timedelta(days=1)

crawl_daterange(start_date,end_date)
