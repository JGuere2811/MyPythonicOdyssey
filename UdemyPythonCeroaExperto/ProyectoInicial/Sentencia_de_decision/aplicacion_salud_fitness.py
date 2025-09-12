print('### Aplicacion de salud y fitness###')
print('....................................')

#constantes
Meta_pasos_diarios = 10000
calorias_por_paso = 0.04

#pedimos los valores al usuario

nombre_usuario = input('Cual es tu nombre ?')
pasos_diarios = int(input('Cuantos pasos has caminado hoy? '))

#verificar si el usuario alcanzo la meta de los pasos diarios
meta_alcanzada = pasos_diarios >= Meta_pasos_diarios
meta_alcanzada_txt = 'Si' if meta_alcanzada else 'No'

#Calculamos las calorias quemadas
calorias_quemadas = pasos_diarios*calorias_por_paso

#mostar la informacion
print(f'..............................')
print(f'Usuario: {nombre_usuario}')
print(f'pasos dados hoy: {pasos_diarios}')
print(f'Calorias quemadas: {calorias_quemadas} kcal')
print(f'Meta de pasos diarios alcanzada: {meta_alcanzada_txt}')
print(f'la meta de pasos diarios es de : {Meta_pasos_diarios} pasos')
