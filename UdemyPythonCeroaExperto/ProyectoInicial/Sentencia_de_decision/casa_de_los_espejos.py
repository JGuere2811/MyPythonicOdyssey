print("###Casa de los Espejos###")
print(".........................")
edad = int(input("Que edad tienes? "))
miedo = input("Te da miedo la oscuridad?(si/no) ").lower == "si"

if(edad > 10 and not miedo):
    print('tienes pase libre')
else:
    print('Lo siento no puedes pasar')

