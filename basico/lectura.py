import json

# Nombre del archivo JSON
filename = 'data.json'

# Abrir el archivo JSON y cargar su contenido
with open(filename, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Imprimir el contenido cargado
print(data)

# Acceder a los datos
print(f"Nombre: {data['name']}")
print(f"Edad: {data['age']}")
print(f"Ciudad: {data['city']}")
print(f"Habilidades: {', '.join(data['skills'])}")
