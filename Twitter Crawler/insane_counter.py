from bs4 import BeautifulSoup
from urllib2 import urlopen
import time

def instagram():
    list_ = []
    result_list = []
    html =  urlopen(instagram_url).read()
    soup = BeautifulSoup(html,'html.parser')
    likes =  soup.find_all('body')
    string = str(likes)
    for i in range(0,len(string)):
        if string[i:i+17] == '"likes":{"count":':
            jackpot =  string[i:i+30]
            list_.append(jackpot)
    for i in range(0, len(list_)):
        number = ''
        for j in range(0,len(list_[i])):
            if list_[i][j] in '0123456789':
                number = number + list_[i][j]
        result_list.append(int(number))

    return result_list

instagram_url = 'https://www.instagram.com/adidas/'

x = instagram()
print(x)
print(len(x))