print("###Sistema de envios###")
destino = str(input("El envio es nacional(1) o internacional(2): ")).strip().lower()
peso = float(input("Cuanto es el peso en Kg del paquete: "))
costo_tarifa = None
if(destino == "nacional" ):
    costo_tarifa = 10
elif(destino == "internacional" ):
    costo_tarifa = 20
else:
    print("opcion no valida")

costo = costo_tarifa*peso
if costo_tarifa is not None:
    print(f"El costo total es de: {costo}")
