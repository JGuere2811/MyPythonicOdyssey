print("###Generación de ticket de venta###")
print("...........................")
#Entrada de datos
precio_leche = float(input("Ingrese el precio de la leche: "))
precio_pan = float(input("Ingrese el precio del pan: "))
precio_lechuga = float(input("Ingrese el precio de la lechuga: "))
precio_platano = float(input("Ingrese el precio del plátano: "))
descuento_porcentraje = int(input("Ingrese el porcentaje de descuento (%): "))

# calculo del subtotal /(sin impuestos)
subtotal= precio_leche + precio_pan + precio_lechuga + precio_platano
# calculo del impuesto por descuento
descuento = subtotal * (descuento_porcentraje / 100)
#subtotal con descuento
subtotal_con_descuento = subtotal - descuento
#calculo del impuesto (IVA 18%)
impuesto = subtotal_con_descuento * 0.18
#calculo de la compra (con impuestos)
total = subtotal_con_descuento + impuesto
#Salida de datos
print(f"""...........................
    subtotal: ${subtotal:.2f}
    descuento ({descuento_porcentraje}%): -${descuento:.2f}
    impuesto (IVA 18%): ${impuesto:.2f}
    total a pagar: ${total:.2f}
""")