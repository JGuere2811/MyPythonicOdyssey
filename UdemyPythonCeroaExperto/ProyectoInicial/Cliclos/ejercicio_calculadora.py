#Comencemos con el titulo
print("*** Aplicacion Calculadora ***")
while True:
    print("""      
    Operaciones que puedes realizar:
    1. Suma
    2. Resta
    3. Multriplicacion
    4. Division
    5. Salir
    Escoge una opcion (1-5): """, end= "")
    opcion =int(input())
    if opcion == 1:
        print("Has escogido la suma")
        num1 = float(input("Ingresa el primer numero: "))
        num2 = float(input("Ingresa el segundo numero: "))
        resultado = num1 + num2
        print(f"El resultado de la suma es: {resultado}\n")
    elif opcion == 2:
        print("Has escogido la resta")
        num1 = float(input("Ingresa el primer numero: "))
        num2 = float(input("Ingresa el segundo numero: "))
        resultado = num1 - num2
        print(f"El resultado de la resta es: {resultado}\n")
    elif opcion == 3:
        print("Has escogido la multiplicacion")
        num1 = float(input("Ingresa el primer numero: "))
        num2 = float(input("Ingresa el segundo numero: "))
        resultado = num1 * num2
        print(f"El resultado de la multiplicacion es: {resultado}\n")
    elif opcion == 4:
        print("Has escogido la division")
        num1 = float(input("Ingresa el primer numero: "))
        num2 = float(input("Ingresa el segundo numero: "))
        if num2 != 0:
            resultado = num1 / num2
            print(f"El resultado de la division es: {resultado}\n")
        else:
            print("Error: No se puede dividir entre cero.\n")
    elif opcion == 5:
        print("Saliendo de la calculadora. ¡Hasta luego!")
        break
    else:
        print("Opcion no valida, por favor escoge una opcion del 1 al 5.\n")
else:
    print("Gracias por usar la calculadora.")