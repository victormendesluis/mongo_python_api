from pymongo import MongoClient

print('Ejecutando python en el contenedor')
#MongoDB
client = MongoClient("mongodb://root:example@mongo:27017")
db=client.apiDB

try: db.command("ServerStatus")
except Exception as e:print(e)
else: print("HAS ENTRADO EN LA MONGO")

def print_options():
    print('LISTA DE TAREAS')
    print('*' * 50)
    print('Selecciona una opción:')
    print('[C]rear una lista')
    print('[L]istado de listas')
    print('[M]odificar lista')
    print('[E]liminar lista')
    print('[S]ALIR')

def run():
    print_options()

    command = input()
    command = command.upper()

    if command == 'C':
        pass
    elif command == 'L':
        pass
    elif command == 'M':
        pass
    elif command == 'E':
        pass
    elif command == 'S':
        os._exit(1)
    else:
        print('Comando inválido')
        time.sleep(1)
        run()

if __name__ == "__main__":
    run()
