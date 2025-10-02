print("### triangulo simetrico 2 en 2 ###")
filas = int(input("Ingrese el numero de filas para el triangulo: "))
# Iterar sobre el rango de filas
#de 2 en 2 simetrico
for i in range(1, filas + 1):
    espacios = ' ' * (filas - i)  # Calcular los espacios necesarios
    asteriscos = '*' * (2 * i - 1)  # Calcular los asteriscos necesarios
    print(espacios + asteriscos)  # Imprimir la fila con espacios y
#de 1 en 1 simetrico
print("### triangulo simetrico de 1 en 1 ###")



# Iterar sobre el rango de filas

for i in range(1, filas + 1):

# Imprimir espacios para centrar el triangulo

    print(' ' * (filas - i), end='')
 # Imprimir asteriscos para formar el triangulo

    print('* ' * i)