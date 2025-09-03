#Receta de cocina
print("Receta de cocina")
print("..................")
# Entrada de datos por consola
nombre_receta = input("Ingrese el nombre de la receta: ")
ingredientes = input("Ingrese los ingredientes (separados por comas): ")
tiempo_preparacion = int(input("Ingrese el tiempo de preparación (en minutos): "))
dificultad = input("Ingrese la dificultad (fácil, media, difícil): ")
print("..................")
# Conversión de datos
dificultad = dificultad.lower()
# Mostrar datos
print(f'Nombre de la receta: {nombre_receta}')
print(f'Ingredientes: {ingredientes}')
print(f'Tiempo de preparación: {tiempo_preparacion} minutos')
print(f'Dificultad (fácil, media, difícil): {dificultad}')
print("..................")
