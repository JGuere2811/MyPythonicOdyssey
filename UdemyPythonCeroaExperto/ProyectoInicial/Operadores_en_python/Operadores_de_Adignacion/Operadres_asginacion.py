print("***Operadores de asignacion***")
numero = 10
print("El valor de numero es:", numero)
#ASignacion variable texto
texto = "Hola, mundo"
print("El valor de texto es:", texto)
#Asignacion de una nueva variable
nuevo_numero = numero
print("El valor de nuevo_numero es:", nuevo_numero)
#Asignacion multriple
variable1, variable2, variable3 = 1, 2, 3
print("El valor de variable1 es:", variable2)
#asignacion ecadenada
a = b = c = 5
print("El valor de a es:", b)
#Intercambio de valores entre variables, sin usar una variable temporal
x, y = 10, 20
y, x = x, y
print("El valor de x es:", x)
print("El valor de y es:", y)
#recibir multiples valores de una función
nombre, edad = input("Ingrese su nombre y edad separados por una coma: ").split(",")
print(f"El nombre ingresado es:{nombre.strip()} y la edad es:{edad.strip()}")