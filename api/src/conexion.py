class conexion:
  def __init__(self, user, password, host, port):
    self.client=MongoClient(f"mongodb://{user}:{password}@{host}:{port}/")
  
  def cerrar_conexion(self):
    self.client.close()

  def traer_bbdd(self):
    return client.apidb
  
