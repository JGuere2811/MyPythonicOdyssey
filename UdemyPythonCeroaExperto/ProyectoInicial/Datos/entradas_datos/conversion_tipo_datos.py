#convertir tipos de datos
#convertir de cadena a entero
cadena_numero = "123"
numero = int(cadena_numero)
suma = numero + 10
print("La suma de", numero, "y 10 es:", suma)
cadena_numero2 = cadena_numero * 10
print(cadena_numero2)
#cconvertir de cadena a flotante
cadena_decimal = "123.45"
decimal = float(cadena_decimal)
suma_decimal = decimal + 10.55
print("La suma de", decimal, "y 10.55 es:", suma_decimal)
cadena_decimal2 = cadena_decimal * 10
print(cadena_decimal2)
#convertir de entero a cadena
numero_entero = 456
cadena_entero = str(numero_entero)
print("El número entero como cadena es:", cadena_entero)
cadena_entero2 = cadena_entero * 5
print(cadena_entero2)

#convertir a boleano
numero_cero = 0.01
booleano_cero = bool(numero_cero)
print(f"El valor booleano de 1 es: {booleano_cero}")
#convertir de cadena a boleano
cadena_vacia = "" # Cadena vacía es considerado 0 osea false
booleano_cadena_vacia = bool(cadena_vacia)
print(f"El valor booleano de una cadena vacía es: {booleano_cadena_vacia}")
#cadena no vacia es considerado 1 osea true
cadena_no_vacia = "Hola"    
booleano_cadena_no_vacia = bool(cadena_no_vacia)
print(f"El valor booleano de una cadena no vacía es: {booleano_cadena_no_vacia}")
#convertir de flotante a entero
decimal_numero = 78.99  
entero_numero = int(decimal_numero)
print(f"El número {decimal_numero} convertido a entero es: {entero_numero}")
#en python no se redondea solo elimina la parte decimal para sacar un entero
#usamos la función round() para redondear
redondeado = round(decimal_numero)
print(f"El número {decimal_numero} redondeado es: {redondeado}")