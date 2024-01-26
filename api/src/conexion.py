from pymongo import MongoClient

class MiConexion:
  def __init__(self, user, password, host, port):
    try:
      # Establece la conexión a la base de datos
      self.client=MongoClient(f"mongodb://{user}:{password}@{host}:{port}/")
      print("Conexión exitosa a la base de datos.")
    except Exception as e:
      print(f"Error al conectar a la base de datos: {e}")

  def abrir_conexion(self):
    self.client=MongoClient(f"mongodb://{user}:{password}@{host}:{port}/")
    
  def cerrar_conexion(self):
    self.client.close()

  def traer_bbdd(self):
    return self.client.apidb
  
