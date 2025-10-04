print('*** Manejo de Sets ***')
#crear un consejo
mi_set = {1, 2, 3, 4, 5, 4} # no acepta elementos duplicados
print(f'Set original: {mi_set}')

#Agregar elementos al set
mi_set.add(6)
mi_set.add(7)
print(f'Mi set modificado: {mi_set}')

#Intertamos agregar un elemento duplicado
mi_set.add(3)

print(f'Mi set modificado: {mi_set}')

mi_set.remove(4) # si el elemento no existe lanza un error
print(f'Mi set modificado: {mi_set}')

for elemento in mi_set:
    print(elemento)

print(f'\n Existe el valor de 1 en el set? {1 in mi_set}  ')

#obtener la longitud del set
print(f'Logitud del conjunto: {len(mi_set)}')