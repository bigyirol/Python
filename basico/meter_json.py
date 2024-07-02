import json
from pymongo import MongoClient

# Conectar a MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Seleccionar la base de datos
db = client['testdb']

# Seleccionar la colección
collection = db['usuarios']

# Leer el archivo JSON
filename = 'data2.json'

with open(filename, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Insertar los datos en la colección
if isinstance(data, list):
    collection.insert_many(data)
else:
    collection.insert_one(data)

print("Datos insertados con éxito.")

# Cerrar la conexión
client.close()
