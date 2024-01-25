from pymongo import MongoClient
from conexion import MiConexion

#MongoDB
user="root"
password="example"
port=27017
host="mongo"
"""
client = MongoClient("mongodb://root:example@mongo:27017")
db=client.apidb
"""
mi_conexion = MiConexion(user, password, host, port)
db=mi_conexion.traer_bbdd()

try: db.command("serverStatus")
except Exception as e:print(e)
else: print("You have access to mongodb")

mi_conexion.cerrar_conexion()
"""
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
def insert(todo):
    db.insert_one({id: todo.id}, {titulo: todo.titulo})

def find_by_id(id):
    todo=db.find({id: id})
    print(todo.id+", "+todo.titulo)
    
def update(todo):
    db.updateOne({id: todo.id}, {$rename{titulo: todo.titulo}})
    
def delete(todo):
    db.deleteOne({id: todo.id})
"""

