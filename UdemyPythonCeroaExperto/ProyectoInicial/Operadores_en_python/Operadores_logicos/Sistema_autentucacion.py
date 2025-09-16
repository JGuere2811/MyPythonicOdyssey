print("###Sistema de autenticacion###")
usuario = str(input("Ingrese el usuario: ")).strip()
password = str(input("Ingrese la contraseña: ")).strip()

if(usuario == "mixas" or password == "JmGc292827"):
    print("Bienvenido al sistema")
else:
    print("Error al iniciar")