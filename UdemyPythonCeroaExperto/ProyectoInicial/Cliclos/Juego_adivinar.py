import random
print("###Juego adivinar el numero###")
numero_aleatorio = random.randint(1,50)
numero_elegido = -1
contador = 0
#Mientras el numero elegido sea diferente al numero aleatorio
while numero_elegido != numero_aleatorio:
    numero_elegido = int(input("Adivina el numero entre el 1 y el 50: "))
    if numero_elegido < numero_aleatorio:
        print("El numero es mayor")
        contador += 1
        print(f"Llevas {contador} intentos")
    elif numero_elegido > numero_aleatorio:
        print("El numero es menor")
        contador += 1
        print(f"Llevas {contador} intentos")
    else:
        print("Felicidades, has adivinado el numero")
        print(f"Lo has logrado en {contador} intentos")