from urllib.request import urlopen
from bs4 import BeautifulSoup
import time,os,sys,csv,re
import pathlib
import datetime

def dataextract(path):
	direc = os.listdir(path)

	file= open('twitter_dec2017_me.csv', 'w',newline='')
	c = csv.writer(file,delimiter=',')
	c.writerow(["Tweet-text","Hashtag-text","Replies","Retweet","Favourites","Hash-Tag","Date-Time","Date","Time"])

	for files in direc:
		url=open(path+"\\"+files,encoding='utf-8')
		html=url.read()
		soup = BeautifulSoup(html, 'html.parser')

		tweets = soup.find_all('li', 'js-stream-item')
		tweet_text=soup.find_all('p','js-tweet-text')
		tweet_reply=soup.find_all('div','ProfileTweet-action--reply')
		tweet_retweet=soup.find_all('div','ProfileTweet-action--retweet')
		tweet_fav=soup.find_all('div','ProfileTweet-action--favorite')
		tweet_timestamps = soup.find_all('a','tweet-timestamp')
		
		for i in range(len(tweet_text)):
			twt_txt=tweet_text[i].text
			find_hash_tag=re.findall(r'#(\w+)',twt_txt)
			hashtag_txt=",".join(find_hash_tag)
			twt_hashtag=len(find_hash_tag)
			twt_rep=tweet_reply[i].find('span','ProfileTweet-actionCountForPresentation').text
			twt_retwt=tweet_retweet[i].find('span','ProfileTweet-actionCountForPresentation').text
			twt_fav=tweet_fav[i].find('span','ProfileTweet-actionCountForPresentation').text
			twt_datetime=tweet_timestamps[i]['title']
			twt_date=twt_datetime.split("-")[1]
			twt_time=twt_datetime.split("-")[0]
			c.writerow([twt_txt,hashtag_txt,twt_rep,twt_retwt,twt_fav,twt_hashtag,twt_datetime,twt_date,twt_time])
		
		url.close()
	file.close()


folder_name=input("Give the name of folder for which data has to be extracted:")
path=os.getcwd()+"\\"+folder_name
dataextract(path)