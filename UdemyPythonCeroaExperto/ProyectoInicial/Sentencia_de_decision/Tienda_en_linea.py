print("###Tienda en linea###")
print("_____________________")
monto = int(input("Cuanto es el total comprado: "))
miembro = str(input("Es miembro(si o no): ").lower())

if(monto > 1000 and miembro == 'si'):

    descuento_porcentaje = 10
    print(f"Felicidades! ganaste el descuento del {descuento_porcentaje}% en total: ")

elif(miembro == 'si'):
    descuento_porcentaje = 5
    print(f"Felicidades! ganaste el descuento del {descuento_porcentaje}% en total: ")

else:
    descuento_porcentaje = 0
    print(f"lo siento tu descuento es de {descuento_porcentaje}% en total: ")

total = monto - monto*descuento_porcentaje/100

print(f'El monto total es de: {total}')