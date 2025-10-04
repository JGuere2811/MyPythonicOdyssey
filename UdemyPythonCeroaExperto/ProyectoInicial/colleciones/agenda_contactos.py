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
      Telefono: {agenda['Manuel']['telefono']}''')