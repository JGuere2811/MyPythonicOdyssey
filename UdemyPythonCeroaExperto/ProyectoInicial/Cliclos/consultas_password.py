import string
#creacion y validacion de password
# Define los conjuntos de caracteres
CARACTERES_ESPECIALES = string.punctuation
MAYUSCULAS = string.ascii_uppercase
NUMEROS = string.digits

while True:
    password = input("Crea tu password (minimo 8 caracteres, especial, mayúscula y número): ")

    # 1. Validación de longitud mínima
    if len(password) < 8:
        print("Error: La contrasena debe tener al menos 8 caracteres. Intenta de nuevo.")
        continue

    # 2. Validación de carácter especial
    tiene_caracter_especial = any(char in CARACTERES_ESPECIALES for char in password)
    if not tiene_caracter_especial:
        print("Error: La contrasena debe contener al menos un caracter especial. Intenta de nuevo.")
        continue

    # 3. Validación de mayúsculas 
    tiene_mayuscula = any(char in MAYUSCULAS for char in password)
    if not tiene_mayuscula:
        print("Error: La contrasena debe contener al menos una letra mayúscula. Intenta de nuevo.")
        continue

    # 4. Validación de números 
    tiene_numero = any(char in NUMEROS for char in password)
    if not tiene_numero:
        print("Error: La contrasena debe contener al menos un número. Intenta de nuevo.")
        continue
        
    # 5. Confirmación de contraseña
    confirmar_password = input("Confirma tu password: ")
    if password != confirmar_password:
        print("Error: Las contrasenas no coinciden. Intenta de nuevo.")
        continue

    # Si todas las validaciones pasan
    print("Password creada exitosamente.")
    break

# --- INICIO DE SESIÓN ---
#validar el password
intentos = 3
while intentos > 0:
    ingreso_password = input("Ingresa tu password para acceder: ")
    
    if ingreso_password == password:
        print("Acceso concedido. Bienvenido!")
        break
    else:
        intentos -= 1
        print(f"Password incorrecta. Te quedan {intentos} intentos.")
else:
    print("Has agotado todos los intentos. Acceso denegado.")