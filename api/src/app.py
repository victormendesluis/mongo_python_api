from pymongo import MongoClient

print('Ejecutando python en el contenedor')
#MongoDB
client = MongoClient("mongodb://root:example@mongo:27017")
db=client.apiDB

try: db.command("ServerStatus")
except Exception as e:print(e)
else: print("HAS ENTRADO EN LA MONGO")
"""
result=db.createCollection("ToDo", {
   validator: {$jsonSchema: {
      bsonType: "object",
      required: ["titulo","descripcion","fecha","terminado","tipo"],
      properties: {
         titulo:{
           bsonType: "string",
           description: "Título de la lista"
         },
         descripcion: {
            bsonType: "string",
            description: "Descripción de la lista"
         },
         fecha: {
            bsonType: "date",
            description: "Fecha en la que se realiza la lista"
         },
         terminado: {
            enum: [ "No", "Si" ],
            description: "Si la lista está acabada o no"
         },
         tipo: {
            enum: [ "Texto", "Audio", "Video" ],
            description: "Tipo de lista"
         }
      }
   }}
})
print(result)
"""
client.close()
