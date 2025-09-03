from random import randint
#Sistema Generador ID Unico
print("Sistema Generador ID Unico")
print("........................")
# Entrada de datos por consola
nombre = input("Ingrese su nombre: ").strip().upper()[0:2]
apellido = input("Ingrese su apellido: ").strip().upper()[0:2]
ano_nacimiento = input("Ingrese su año de nacimiento: ")
print("........................")
# Conversion de datos
ano_nacimiento = int(ano_nacimiento)
ultimos_digitos_año = str(ano_nacimiento)[-2:]
numero_aleatorio = str(randint(1000, 9999))
# Mostrar id generado
id_generado = f'{nombre}{apellido}{ultimos_digitos_año}{numero_aleatorio}'
print(f'Su ID unico generado es: {id_generado}')