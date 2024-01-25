from pymongo import MongoClient

print('Ejecutando python en el contenedor')
#MongoDB
client = MongoClient("mongodb://root:example@mongo:27017")
db=client.apidb

try: db.command("serverStatus")
except Exception as e:print(e)
else: print("You have access to mongodb")

def create_collection():
    db.createCollection("todo", {
        validator: {$jsonSchema: {
            bsonType: "object",
            required: ["id","titulo"],
            properties: {
                id: {
                    bsonType: "int",
                    description: "id del todo"
                },
                titulo: {
                    bsonType: "string",
                    description: "titulo del todo"
                },
                descripcion: {
                    bsonType: "string",
                    description: "descripción del todo"
                },
                fecha: {
                    bsonType: "string",
                    description: "descripción del todo"
                },
                terminado: {
                    bsonType: "bool",
                    description: "enum para ver el estado del todo"
                },
                tipo: {
                    enum: [ "Texto", "Audio","Imagen","Video" ],
                    description: "tipo de todo"
                }
            }
        }}
    })
