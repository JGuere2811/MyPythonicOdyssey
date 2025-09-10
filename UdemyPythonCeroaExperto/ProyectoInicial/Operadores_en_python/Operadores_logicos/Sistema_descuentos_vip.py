#sistema deescuentos para clientes vip
print("###Sistema de descuentos para clientes VIP###")
print(".............................................")
cliente_vip = input("¿Es usted un cliente VIP? (si/no): ").lower() == 'si'
cantidad_mayor_10 = float(input("Ingrese la cantidad de articulos de su compra: ")) >= 10
print(".............................................")
#si el cliente es vip o la compra es mayor a 10 entonces tiene descuento
tiene_descuento = cliente_vip and cantidad_mayor_10
print(f"¿Tiene descuento? {tiene_descuento}")
print(".............................................")

print(cantidad_mayor_10)