print("###Sistema de calificaciones###")
nota = float(input("Ingrese la nota: "))
if(9 <= nota <= 10):
    nota_letra = "A"
elif(8 <= nota < 9):
    nota_letra = "B"
elif(7 <= nota < 8):
    nota_letra = "C"
elif(6 <= nota < 7):
    nota_letra = "D"
elif(0 <= nota < 6):
    nota_letra = "F"
else:
    nota_letra = "valor desconocido"

print(f"La nota que sacaste es de {nota_letra}")