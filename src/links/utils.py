import requests
from bs4 import BeautifulSoup
import lxml

def get_link_data(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
        'Accept-Language' : "en",
    }

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text,"lxml")
    # print(soup.prettify())

    name = soup.select_one(selector="#productTitle").getText().strip()
    # print(name)
    price = float(soup.select_one(selector="#priceblock_ourprice").getText()[1:].replace(",",""))
    # print(price)
    return name,price