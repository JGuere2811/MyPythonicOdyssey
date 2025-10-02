print("### Validacion campo de un formulario ###")

nombre_usuario = None

while not nombre_usuario:
    nombre_usuario = input("Ingrese su nombre de usuario (minimo 3 caracteres): ")
    if len(nombre_usuario) < 3:
        print("Error: El nombre de usuario debe tener al menos 3 caracteres. Intenta de nuevo.")
        nombre_usuario = None
print(f"Nombre de usuario '{nombre_usuario}' registrado exitosamente.")