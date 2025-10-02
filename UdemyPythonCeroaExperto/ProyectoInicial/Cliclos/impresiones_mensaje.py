print("### Repeticiones e impresiones de mensajes ###")

mensaje = input("Ingrese un mensaje: ")
veces = int(input("Cuantas veces desea imprimir el mensaje? "))

# Usando un ciclo for
for i in range(veces):
    print(f"{i+1}-{mensaje}")