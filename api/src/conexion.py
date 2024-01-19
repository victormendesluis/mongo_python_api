class conexion:
  def __init__(self, user, password, host, port):
    self.client=MongoClient()
  def cerrar_conexion(self)
    self.client.close()
