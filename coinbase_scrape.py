from bs4 import BeautifulSoup
import requests
import urllib.request, json

coinbase_url = urllib.request.urlopen('https://www.coinbase.com/browse').read()
soup = BeautifulSoup(coinbase_url, 'lxml')
print(soup.prettify())