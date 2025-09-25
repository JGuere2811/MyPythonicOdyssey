print("*** Aplicacion Cajero Automatica ***")
saldo = 1000

salir = False      
while not salir:
    print(f'Saldo actual: ${saldo}')
    print('''
    Menu:
    1. Ingresar dinero
    2. Retirar dinero
    3. Salir''')
    opcion = int (input('Ingrese una opcion:'))
    if opcion == 1:
        agregar = float(input('Ingrese la cantidad a ingresar: '))
        saldo += agregar
        print('Ingresando dinero...\n')
        print(f'Se han ingresado ${agregar} a su cuenta\n')
        print(f'Su nuevo saldo es: ${saldo}\n')
    elif opcion == 2:
        while True:
            
            entrada = input('Ingrese la cantidad a retirar (o S para salir): ')

            if entrada.upper() == 'S':
                print('Saliendo...\n')
                #salir = True
                break

            try:
                retirar = float(entrada)

            except ValueError:
                print('Por favor ingrese un numero valido\n')

                continue
        
            if retirar <= saldo:
                saldo -= retirar
                print(f'Se han retirado ${retirar} de su cuenta\n')
                print(f'Su nuevo saldo es: ${saldo}\n')
                print('Retirando dinero...\n')
                break
            else:
                print('No tiene suficiente saldo para retirar esa cantidad\n')
    elif opcion == 3:
        print('Saliendo...\n')
        break
    else:
        print('Opcion incorrecta\n')
else:
    print('Gracias por usar el sistema')