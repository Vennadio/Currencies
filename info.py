import requests
from bs4 import BeautifulSoup

url = 'https://cbr.ru/currency_base/daily/'
headers = {
    'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 Edg/89.0.774.77'
}


def callback():
    data = ''
    response = requests.get(url, headers)
    soup = BeautifulSoup(response.text, 'lxml')
    currents = []
    blocks_currencies = soup.find_all("tr")
    for block in blocks_currencies:
        info = block.find_all("td")
        if len(info) != 0:
            #code = info[0].text
            code_letter = info[1].text
            units = info[2].text
            currency = info[3].text
            course = info[4].text
            data += ("--------------------------\n"
                     #f"Цифр.код - {code}\n"
                     f"Букв.код - {code_letter}\n"
                     f"Единиц - {units}\n"
                     f"Валюта - {currency}\n"
                     f"Курс - {course}\n")
    return data
