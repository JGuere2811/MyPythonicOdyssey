print("###Valor dentro de un rango###")
print("...........................")
valor = int(input("Ingrese un valor entero dentro (0-5): "))
#Revisar si el valor se encuentra dentro del rango de 0 a 5
valor_dentro_rango = valor >= 0 and valor <= 5
print(f"¿El valor {valor} se encuentra dentro del rango de 0 a 5? {valor_dentro_rango}")
print("...........................")