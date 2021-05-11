from bs4 import BeautifulSoup
import requests

url = 'https://trends.rbc.ru/trends/education/?utm_source=topline'
header = {
    'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56'
}
def get():
    result = ''
    link = ''
    response = requests.get(url,header)
    get = BeautifulSoup(response.text,'lxml')
    news = get.find(class_ = 'l-window l-window-overflow-mob')
    link = get.find_all('href')
    #print (f'{type(news.text)}\t')
    info = news.find_all(class_='l-base__col__25p')
    print (f'{len(info)}')
    #print (info[0].find('a').get('href'))
    for j in info:
        #print(j.find('a',class_='item__title').text)
        #print(j.find('a').get('href'))
        l = j.find('a', class_='item__title').text
        z = j.find('a').get('href')
        result += (f"{l}"
                   f"{z}")
    return result