from pymongo import MongoClient

print('Ejecutando python en el contenedor')
#MongoDB
client = MongoClient("mongodb://root:example@mongo:27017")
db=client.apiDB

try: db.command("ServerStatus")
except Exception as e:print(e)
else: print("HAS ENTRADO EN LA MONGO")

result=db.createCollection("contacts", {
   validator: {$jsonSchema: {
      bsonType: "object",
      required: ["phone"],
      properties: {
         phone: {
            bsonType: "string",
            description: "must be a string and is required"
         },
         email: {
            bsonType: "string",
            pattern: "@mongodb\.com$",
            description: "must be a string and match the regular expression pattern"
         },
         status: {
            enum: [ "Unknown", "Incomplete" ],
            description: "can only be one of the enum values"
         }
      }
   }}
})
print(result)

client.close()
