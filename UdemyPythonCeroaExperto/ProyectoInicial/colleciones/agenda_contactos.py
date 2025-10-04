print('***Agenda de Contactos***')

agenda = {
    'Manuel': {
        'telefono': '9235148362',
        'email': 'mixas@gmail.com',
        'direccion': 'Calle falsa 123'
    },
    'Khiara': {
        'telefono': '9626344872',
        'email': 'khi9601@gmail.com',
        'direccion': 'Avenida siempre viva 742'
    },
    'Fatyma': {
        'telefono': '9648274543',
        'email': 'fatymonchis@gmail.com',
        'direccion': 'av. mariscal castilla 123'
    }
}
print('Contactos en la agenda:')
print(agenda)
#Acceder a la informacion de un contacto en especifico
print(f'''\nInformacion de contacto de manuel:
    Telefono: {agenda['Manuel']['telefono']}
    Email: {agenda.get('Manuel').get('email')}
    direccion: {agenda['Manuel']['direccion']}  
    ''')
#Agregar un nuevo contacto
agenda['Marilin'] = {
    'telefono': '9234567890',
    'email': 'marilin@gmail.com',
    'direccion': 'Calle 8 # 123'
    }
print(agenda)

#Eliminar un contacto existente
agenda.pop('Fatyma')
print(agenda)

#Mostrar los contactos de la agenda
print('\n Contactos en la angenda: ')
for nombre, detalles in agenda.items():
    print(f'''Nombre: {nombre}
    Telefono: {detalles.get('telefono')}
    Email: {detalles.get('email')})
    Direccion: {detalles.get('direccion')}
    ''')
