from pymongo import MongoClient

#MongoDB
client = MongoClient("mongodb://root:example@mongo:27017")
db=client.apiDB

try: db.command("ServerStatus")
except Exception as e:print(e)
else: print("HAS ENTRADO EN LA MONGO")

client.close()
