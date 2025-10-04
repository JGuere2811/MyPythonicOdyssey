print('### playlist de canciones ###')

#creamos la lista vacia
lista_reproduccion = []

numero_canciones = int(input('Cuantas canciones deseas agregar a la lista de reproduccion? '))

#Solicitamos las canciones al usuario
for i in range(numero_canciones):
    cancion = input(f'Ingresa el nombre de la cancion {i+1}: ')
    lista_reproduccion.append(cancion)

#Empezamos a agregar canciones
#lista_reproduccion.append('Hotel California  - eaagles')
#lista_reproduccion.append('Imagine - John Lennon')
#lista_reproduccion.append('Smells Like Teen Spirit - Nirvana')

#lista_reproduccion.sort(reverse= True)

#print(f'\n Lista de reproduccion: ')
#print(lista_reproduccion)

print('\n Canciones en la lista de reproduccion:')
for cancion in lista_reproduccion:
    print(f'- {cancion}')