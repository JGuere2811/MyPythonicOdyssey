print("###Sistema Reserva Hotel###")
print("...........................")
nombre_cliente = str(input("Cual es el nombre ?"))
dias_estadia = int(input("Cuantos dias estara en el hotel?"))
vista_mar = input("Tu cuarto tiene vista al mar(si/no)?").lower().strip() == "si"
vista_con_mar = 190.50
vista_sin_mar = 150.50
#procesamiento
if vista_mar:
    costo = vista_con_mar
else:
    costo = vista_sin_mar

costo_total = dias_estadia * costo
#mostramos los detalles
print(f"......................................")
print(f"Estimado usuario {nombre_cliente} este es su resumen")
print(f"la cantidad por cuarto es de: {costo}")
print(f"Los dias son: {dias_estadia}")
print(f"EL total seria: {costo_total}")
