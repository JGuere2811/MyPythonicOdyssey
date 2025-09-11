print("###Sistema de autenticación###")
print("...................................")
usuario = str("mixas")
contraseña = 1234
ingreso_usuario = input("Ingrese su usuario: ")
ingreso_contraseña = int(input("Ingrese su contraseña: "))
#Verificar si el usuario y la contraseña son correctos
autenticacion_correcta = ingreso_usuario == usuario and ingreso_contraseña == contraseña
print("...................................")
print(f"¿El usuario y la contraseña son correctos? {autenticacion_correcta}")
print("...................................")