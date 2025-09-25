print('*** Sistema de administracion de cuentas ***')

salir = False

while not salir:
    print('''Menu:
    1. Crear cuenta
    2. Eliminar Cuenta
    3. Salir''')
    opcion = int (input('Ingrese una opcion:'))
    if opcion == 1:
        print('Creando tu cuenta...\n')
    elif opcion == 2:
        print('Eliminando tu cuenta...\n')
    elif opcion == 3:
        print('Saliendo...\n')
        salir = True
    else:
        print('Opcion incorrecta\n')

else:
    print('Gracias por usar el sistema')