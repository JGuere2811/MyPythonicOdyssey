print("###calcular área y perímetro de un rectángulo###")
print("..........................................")
base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))
#Calcular el área y perímetro del rectángulo
area = base * altura
perimetro = 2 * (base + altura)
#Salida de datos
print(f"""..........................................
    Área del rectángulo: {area}
    Perímetro del rectángulo: {perimetro}
""")
print("..........................................")