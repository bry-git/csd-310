from http import client
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.ahowo.mongodb.net/admin?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

def get_collections_from_atlas(): 
    collections = db.list_collection_names()

    print("")
    print("- - pytech Collection List - -")
    print(collections)

    input("end of program, press any key to exit")
    

get_collections_from_atlas()

