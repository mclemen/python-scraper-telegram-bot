import urllib.request, json
from pymongo import MongoClient

# connection_string = "mongodb://192.168.33.10:27017"
# client = MongoClient(connection_string)
# dbase = client.get_database("")

url = urllib.request.urlopen("https://www.coinbase.com/api/v2/assets/").read()

data = json.loads(url)
for i in range(len(data["data"])):
    print("Name: " + data["data"][i]['assetName'])
    print("Symbol: " + data["data"][i]['assetCode'])
    print(" ")