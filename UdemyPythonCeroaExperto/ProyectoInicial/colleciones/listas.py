print("*** Manejo de Listas ***")
# Definicion de una lista
lista = [ 1, 2, 3, 4, 5]

#largo de una lista
print(f'{lista} -> lista original')

#Acceder a  los elementos de la lista por indice

print(f'Acceder al valor del indice 4: {lista[4]} ')
print(f'Acceder el ultimo indice de la lista: {lista[-1]}')


#modificar los elemenotos de una lista
lista[1] = 10
print(f'modificamos el valor del indice 1 : {lista[1]}-> {lista}')

#anadir un  nuevo elelmento en un indice especifico
lista.insert(2, 15)
print(f'{lista}-> se anadio el valor de 15 en el inidice 2')

#eliminar elementos de una lista
#usando el metodo remove
lista.remove(5)
print(f'{lista} -> Se removio el valor 5')
# Remover por indice con el motodo pop
elemento = lista.pop(1)
print(f'{lista} -> Se elimino el indice 1')
print(lista)
print(elemento) #se guardor eliminado en la variable
#eliminar usando la palabra del 
del lista[2]
print(f'{lista} -> se elimino el indice 2 ')# no se recupera el valor eliminado
#obtener sublista
sublista = lista[1:3] #genera una sublista del indice 1 al 2 (3 no se incluye)
print(f'sublista del indice 1 al 2: {sublista}')