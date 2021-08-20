# import os
# from binance.client import Client

# api_key = '8cS37kWxlRmLuDXycpUyBGN0kcagyN1Em59JfJNBxDWJrwdOf0vwIJxqCcpvE6G6'
# api_secret = 'KP0OL8We8oM2KH9KqNsLvsPoD0un97tL3RivcDofdIpzXmdsNhw5qn4Q6sHjpt6N'

# client = Client(api_key, api_secret)

# client.API_URL = 'https://api.binance.com/api/v3/exchangeInfo'

# exchange_info = client.get_exchange_info()

# for s in exchange_info['symbols']:
#     print(s['symbol'])


from bs4 import BeautifulSoup
import requests
# import time
import urllib.request
import lxml.html


def new_list():
    binance_url = urllib.request.urlopen('https://www.binance.com/en/support/announcement/c-48').read()
    soup = BeautifulSoup(binance_url, 'lxml')
    new_coin_list = soup.find(class_ = 'css-1ej4hfo')
    # print(new_coin_list.text.strip())
    return new_coin_list.text.strip()

if __name__ == "__main__":
    print(new_list())

