print('*** Diccionarios en python ***')
#Creamos un dict de persona con clave y valor
personas = {
    'nombre': 'Sergio',
    'edad': 30,
    'Ciudad': 'Mexico'
}
print(f'Diccionario de personas {personas}')

#Acceder a los elementos del dioccionario
print(f'Nombre: {personas['nombre']}')
print(f'Edad: {personas.get('edad')}')
print(f'Ciudad: {personas.get('Ciudad')}')

#Modificar un valor del diccionario
personas['edad'] = 35
print(f'Diccionario modificado: {personas}')

#Agregar un nuevo elemento
personas['profesion'] = 'Ingeniero'
print(f'Diccionario con nuevo elemento: {personas}')

#Eliminar un elemento
del personas['Ciudad']
print(f'Diccionario con elemento eliminado: {personas}')

personas.pop('profesion')
print(f'Diccionario de personas: {personas}')
#Interaccion los elementos de un dict(llave, valor)
for llave, valor in personas.items():
    print(f'Llave: {llave},valor: {valor}')
#Obtener todas las llaves
print(f'\nValores del diccionario: ')
for valor in personas.values():
    print(f'-valor: {valor}')
#Obtener todos los valores
print(f'\n Llaves del diccionario: ')
for llave in personas.keys():
    print(f'- llave: {llave}')