#formato de cadenas
nombre = "Juan"
edad = 30
#formato con f-string (Python 3.6+)
mensaje = f"Hola, mi nombre es {nombre} y tengo {edad} años."
print(mensaje)
#formato con metodo format
mensaje2 = "Hola, mi nombre es {} y tengo {} años.".format(nombre, edad)
print(mensaje2)