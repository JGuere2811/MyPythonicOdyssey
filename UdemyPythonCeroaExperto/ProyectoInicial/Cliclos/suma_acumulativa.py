print("*** Suma Acumulativa***")
# suma acumulativa

Maximo = 5
numero = 1
acumulador = 0

#Empezamos a iterar

while numero <= Maximo:
    #imprimir lo se va a sumar
    print(f'(+ {numero})', end=" ")
    acumulador += numero
    numero += 1
    print(f' = {acumulador}')

print(f'\nResultado suma acumulada: {acumulador}')