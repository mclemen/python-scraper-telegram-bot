import cbpro
from pymongo import MongoClient

def new_list():
    mongo_server = "mongodb://192.168.33.10:27017/"
    client = MongoClient(mongo_server)
    dbase = client.get_database("crypto_coins")
    collection = dbase["coinbase_lists"]

    public_client = cbpro.PublicClient()
    data = public_client.get_products()

    collection.create_index('id', unique = True)
    collection.insert_many(data)

    for coin_lists in collection.find({}, {"id": 1, "base_currency": 1}):
        print(coin_lists)

if __name__ == "__main__":
    print(new_list())


# for i in data:
#     lists = i["display_name"] 
#     # print("ID: ", i["id"])
#     # print("Name: ", i["display_name"])
#     # print("Base Currency: ", i["base_currency"])
#     # print(" ")
#     print(lists)