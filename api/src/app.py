from pymongo import MongoClient

print('Ejecutando python en el contenedor')
#MongoDB
client = MongoClient("mongodb://root:example@mongo:27017")
db=client.apiDB

try: db.command("ServerStatus")
except Exception as e:print(e)
else: print("HAS ENTRADO EN LA MONGO")

result=db.createCollection("ToDo", {
   validator: {$jsonSchema: {
      bsonType: "object",
      required: ["descripcion","fecha","terminado"],
      properties: {
         descripcion: {
            bsonType: "string",
            description: "decripcion del to do"
         },
         fecha: {
            bsonType: "date",
            description: "tiene que ser una fecha valida"
         },
         terminado: {
            enum: [ "No", "Si" ],
            description: "solo puede ser una de las opciones"
         }
      }
   }}
})
print(result)

client.close()
