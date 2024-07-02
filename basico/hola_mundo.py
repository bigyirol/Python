print("hola mundo")
# Nombre del archivo
filename = 'example.txt'

# Contenido a escribir en el archivo
content = 'Este es un ejemplo de cómo escribir en un archivo usando Python. \nVamos a comprobar si esto realmente funciona o no'

# Abrir el archivo en modo escritura ('w' para escribir)
with open(filename, 'w', encoding='utf-8') as file:
    # Escribir el contenido en el archivo
    file.write(content)

print(f'Contenido escrito en {filename}')
