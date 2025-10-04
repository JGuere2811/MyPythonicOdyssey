print("*** Manejo de tuplas ***")

mi_tupla = (1, 2, 3, 4, 5)
print(f'Tupla original: {mi_tupla}')
#mi_tupla[0] = 10
#mi_tupla.append(6)

#Iteramos los elementos de una tupla
for elemento in mi_tupla:
    print(elemento)
coordenadas = (3, 5)
#crear una tupla para coordenadas x,y
print(f'\n coordenada en el eje x : {coordenadas[0]}')
print(f'coordenada en el eje y : {coordenadas[1]}')
#crear una tupla unitaria
tupla_un_elemento = 10,
print(f'\n Tupla unitaria: { tupla_un_elemento}')
#tuoka anidada
tupla_anidada = (1, (2,3), (4,5))
print(f'\n Tupla anidada: {tupla_anidada[1]}')