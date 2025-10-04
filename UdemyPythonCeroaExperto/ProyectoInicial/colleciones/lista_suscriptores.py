print('*** Lista de Suscriptores ***')
#definimos el set inicial
#suscriptores = {} #aqui se define un diccionario vacio

suscriptores = set()

numero_suscriptores = int(input('Proporciona el numero de suscripciones iniciales: '))


suscriptores = {'liusa@gmail.com','marcos@gmail.com','elena@gmail.com'}
for _ in range(numero_suscriptores):
    suscriptores.add(input('Nuevo suscritor (email)'))
print(f'Lista de suscriptores: [suscriptores]')
#verificar si un nuevo suscriptor ya esta en la lista 
nuevo_suscriptor = input('Proporciona el correo del nuevo suscriptor: ')
if nuevo_suscriptor in suscriptores:
    print(f'El correo {nuevo_suscriptor} ya esta en la lista de suscriptores')
else:
    suscriptores.add(nuevo_suscriptor)
    print(f'El correo {nuevo_suscriptor} fue agregado a la lista de suscriptores')
print(f'Lista actualizada de suscriptores: {suscriptores}') 
#eliminar un suscriptor
suscriptor_eliminar = input('Proporciona el correo del suscriptor a eliminar: ')
suscriptores.remove(suscriptor_eliminar)
print(f'El correo {suscriptor_eliminar} fue eliminado de la lista de suscriptores')
print(f'Lista actualizada de suscriptores: {suscriptores}')
#verificar la cantidad de suscriptores
print(f'Cantidad de suscriptores: {len(suscriptores)}')

#Mostar todos los suscriptores
print('Lista de suscriptores:')
for suscriptor in suscriptores:
    print(f'- {suscriptor}')