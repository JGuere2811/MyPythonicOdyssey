print("### break y continue en ciclos ###")

# Ejemplo con break
for numero in range(1, 11):
    if numero % 2 == 0:
        print(numero)
        break #sale del ciclo inmediato
#ejemplo con continue
for numero in range(1, 10):
    if numero % 2 == 0 : # numero impar
        continue #salta a la siguiente iteracion