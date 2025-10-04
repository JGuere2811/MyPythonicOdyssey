print('*** Combinacion de lista y tuplas ***')

#desfinir una lista que almacena tuplas
productos = [
    ('P001', 'Camiseta', 20.0),
    ('P002', 'Jeans', 30.0),
    ('P003', 'Sudadera', 40.0)
]

#imprimir la informacion de cada producto
# y ademas calculamos el precio total
precio_total = 0
print('Informacion de los productos: ')
for producto in productos:
    #print(producto)
    id, descripcion, precio = producto #unpacking
    print(f'Producto: id = {id}, descripcion = {descripcion}, precio = {precio}')
    precio_total += precio #producto[2]
print(f'Precio total de los productos: {precio_total}')