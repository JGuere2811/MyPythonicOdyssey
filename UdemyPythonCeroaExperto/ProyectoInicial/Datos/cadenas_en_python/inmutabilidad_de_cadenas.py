#Inmtabilidad en cadenas 
cadena1 = 'Hola mundo'
#cadena1[0] = 'h'  # Esto generará un error porque las cadenas son inmutables
cadena2 = cadena1
cadena1 = 'adios mundo'  # Esto crea una nueva cadena y asigna a cadena1
print("cadena1:", cadena1)
print("cadena2:", cadena2)
# Intentar modificar un caracter de la cadena generará un error
