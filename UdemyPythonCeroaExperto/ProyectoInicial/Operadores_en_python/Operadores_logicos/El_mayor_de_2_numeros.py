print("###El mayor de 2 numeros###")
numero1 = input("Ingrese el primer numero: ")
numero2 = input("Ingrese el segundo numero: ")
#hacemos el procedimiento
if(numero1 > numero2):
    print(f"El numero {numero1} es mayor que {numero2}")
elif(numero2 > numero1):
    print(f"El numero {numero2} es mayor que {numero1}")
else:
    print(f"El numero {numero2} es igual que {numero1}")