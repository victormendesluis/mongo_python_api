from pymongo import MongoClient

print('Ejecutando python en el contenedor')
#MongoDB
client = MongoClient("mongodb://root:example@mongo:27017")
db=client.apidb

try: db.command("serverStatus")
except Exception as e:print(e)
else: print("HAS ENTRADO EN LA MONGO")

def print_options():
