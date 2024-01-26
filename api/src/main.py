"""from pymongo import MongoClient"""
from conexion import MiConexion
from todo import MiTodo
"""import jsonchema"""

#MongoDB
user="root"
password="example"
port="27017"
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
"""
todo_schema = {
    'validator': {
        '$jsonSchema': {
            'bsonType': 'object',
            'required': ['id', 'titulo'],
            'properties': {
                'id': {
                    'bsonType': 'int',
                    'description': 'id del todo'
                },
                'titulo': {
                    'bsonType': 'string',
                    'description': 'titulo del todo'
                },
                'descripcion': {
                    'bsonType': 'string',
                    'description': 'descripción del todo'
                },
                'fecha': {
                    'bsonType': 'string',
                    'description': 'fecha del todo'
                },
                'terminado': {
                    'bsonType': 'bool',
                    'description': 'enum para ver el estado del todo'
                },
                'tipo': {
                    'enum': ['Texto', 'Audio', 'Imagen', 'Video'],
                    'description': 'tipo de todo'
                }
            }
        }
    }
}
"""
documento={"name":"Juan"}
collection=db.todo
collection.insert_one(documento)
mi_conexion.cerrar_conexion()
"""
db.todo.insert_one({id: 7}, {"name": "MiLista"})
db.todo.find().pretty()
db.todo.findOneAndDelete({id:7})
db.todo.find().pretty()

# Insertar documentos
documents = [
    {
        'id': 1,
        'titulo': 'Hacer compras',
        'descripcion': 'Comprar víveres para la semana',
        'fecha': '2024-01-26',
        'terminado': False,
        'tipo': 'Texto'
    },
    {
        'id': 2,
        'titulo': 'Preparar presentación',
        'descripcion': 'Preparar la presentación para el cliente',
        'fecha': '2024-01-27',
        'terminado': True,
        'tipo': 'Texto'
    }
]

db.todo.insert_many(documents)

# Mostrar datos
cursor = db.todo.find()
for document in cursor:
    print(document)

"""
"""   
def insert(todo):
    db.insertOne({id: todo.id}, {titulo: todo.titulo})

def find_by_id(id):
    todo=db.find({id: id})
    print(todo.id+", "+todo.titulo)
    
def update(todo):
    db.updateOne({id: todo.id}, {$rename{titulo: todo.titulo}})
    
def delete(todo):
    db.deleteOne({id: todo.id})
"""
