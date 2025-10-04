print("*** Calculo de Promedio de Calificaciones ***")
# Definicion de una lista de calificaciones
calificaciones = []
numero_calificaciones = int(input("Cuantas calificaciones deseas ingresar? "))
for i in range(numero_calificaciones):
    calificacion = float(input(f'Ingresa la calificacion {i+1}: '))
    calificaciones.append(calificacion)
print(f'Calificaciones ingresadas: {calificaciones}')

# Calculo del promedio
promedio = sum(calificaciones) / len(calificaciones)
print(f'El promedio de las calificaciones es: {promedio:.2f}')
# Determinar la calificacion mas alta y mas baja
calificacion_mas_alta = max(calificaciones)
calificacion_mas_baja = min(calificaciones)
print(f'La calificacion mas alta es: {calificacion_mas_alta}')
print(f'La calificacion mas baja es: {calificacion_mas_baja}')