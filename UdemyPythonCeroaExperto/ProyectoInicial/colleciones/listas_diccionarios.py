print('*** Listas y Diccionarios ***')

personas = [
    {
        'Nombre': 'Manuel',
        'Apellido': 'Guere',
        'Edad': 24
    },
    {
        'Nombre': 'Khiara',
        'Apellido': 'Romero',
        'Edad': 24
    },
    {
        'Nombre': 'Fatyma',
        'Apellido': 'Ore',
        'Edad': 25
    }
]

print(personas)
#Acceder a un diccionario desde una lista
print(f'''
    Nombre: {personas[0].get('Nombre')}
    Apellido: {personas[0].get('Apellido')}
    Edad: {personas[0].get('Edad')}
''')
#Recorrer los elementos de la lista
print()
for contador, persona in enumerate(personas):
    print(f'{contador}- Persona: {persona}')
    #print(f'Detalles: Nombre: {persona.get("Nombre")}, Apellido: {persona.get("Apellido")}, Edad: {persona.get("Edad")}')