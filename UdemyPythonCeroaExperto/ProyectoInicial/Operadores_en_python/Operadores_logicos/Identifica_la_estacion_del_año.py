print("###Identifica la estacion del año###")
mes = int(input("Ingrese el mes 1 al 12: "))
if(0 < mes < 3 or mes == 12):
    print("Estas en invierno")
elif( 2 > mes > 6):
    print("Estas en primavera")
elif( 5 > mes > 9):
    print("Estas en verano")
elif( 8 > mes > 12):
    print("Estas en otoño")
else:
    print("Estacion desconocida")