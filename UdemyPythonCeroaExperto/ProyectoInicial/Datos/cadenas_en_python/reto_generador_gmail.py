
print("*** Generador de correos electrónicos tipo Gmail ***")
#ingresar nombre de usuario y guardarla en la variable nombre_usuario
nombre_usuario = input("Ingrese su nombre de usuario: ")
#se remplazan los espacios por puntos y se convierte a minúsculas
nombre_normalizado = nombre_usuario.replace(" ", ".").lower().strip()
#se ingresa el nombre de la empresa y la extensión del dominio
nombre_empresa = input("Ingrese el nombre de la empresa: ")
extension_dominio = input("Ingrese la extensión del dominio (por ejemplo '.com.mx'): ")
#se remplazan los espacios y se convierte a minúsculas
dominion_normalizado = nombre_empresa.replace(" ", "").lower().strip()+extension_dominio.lower().strip()
#se genera el correo electrónico
correo_electronico = f"{nombre_normalizado}@{dominion_normalizado}"
#se muestra el correo electrónico generado
print("Su correo electrónico generado es:", correo_electronico)

