print("Hello World, Hola Mundo. Hola, Night City")

from pymongo import MongoClient

client = MongoClient("mongodb://root:example@mongo:27017")
db=client.testdb

try: db.command("ServerStatus")
except Exception as e:print(e)
else: print("HAS ENTRADO EN LA MONGO")

client.close()
