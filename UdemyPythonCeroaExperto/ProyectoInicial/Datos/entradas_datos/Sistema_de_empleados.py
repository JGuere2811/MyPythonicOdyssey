print("Sistema de empleados")
print("........................")
# Entrada de datos por consola
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
salario = input("Ingrese su salario: ")
condicion = input("¿Es jefe de departamento? (Si/No): ")
print("........................")
# Conversion de datos
edad = int(edad)
salario = float(salario)
condicion = condicion.lower() == 'si' 
#si pones lower() conviertes todo a minúsculas entonces ya no es
#necesario poner "Si" con mayúscula o otra forma de escribirlo
print("........................")
# Mostrar datos
print(f'Nombre: {nombre}')
print(f'Edad: {edad} años')
print(f'Salario: ${salario}')
print(f'Jefe de departamento: {condicion}')
print("........................")