#ggenerador de emails
print("Sistema Generador de Emails")
print("........................") 
nombre = input("Ingrese su nombre: ").strip().lower().replace(" ", ".")
apellido = input("Ingrese su apellido: ").strip().lower().replace(" ", ".")
empresa = input("Ingrese el nombre de la empresa: ").strip().lower().replace(" ", "")
extension = input("Ingrese la extensión del dominio (por ejemplo '.com.mx'): ").strip().lower()
print("........................")
#generar email
email = f"{nombre}.{apellido}@{empresa}{extension}"
print(f'Su email generado es: {email}')
print("........................")