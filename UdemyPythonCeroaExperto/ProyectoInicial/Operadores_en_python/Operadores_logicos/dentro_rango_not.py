#Revisa si una variable se encuentra dentro de un rango
print("###Dentro de un rango###")
print("...........................")
dato = int(input("Ingrese un dato entero: "))

#Revisar si el dato se encuentra dentro del rango de 1 a 10
#dentro_rango = dato >= 1 and dato <= 10
#print(f"¿El dato {dato} se encuentra dentro del rango de 1 a 10? {dentro_rango}")

#revisar si el dato NO se encuentra dentro del rango de 1 a 10
dentro_rango = not (dato >= 1 and dato <= 10)
print(f"¿El dato {dato} NO se encuentra dentro del rango de 1 a 10? {dentro_rango}")
print("...........................")