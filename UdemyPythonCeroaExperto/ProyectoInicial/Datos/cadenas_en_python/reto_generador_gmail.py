nombre_usuario = input("Ingrese su nombre de usuario: ")
nombre_normalizado = nombre_usuario.replace(" ", ".").lower()
nombre_empresa = input("Ingrese el nombre de la empresa: ")
extension_dominio = input("Ingrese la extensión del dominio (por ejemplo '.com.mx'): ")
dominion_normalizado = nombre_empresa.replace(" ", "").lower()+extension_dominio.lower()
correo_electronico = f"{nombre_normalizado}@{dominion_normalizado}"
print("Su correo electrónico generado es:", correo_electronico)

