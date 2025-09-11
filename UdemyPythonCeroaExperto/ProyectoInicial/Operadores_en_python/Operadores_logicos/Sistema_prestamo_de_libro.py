print("###Sistema de préstamo de libros###")
print("...................................")
Credencial_estudiante = input("¿Tiene credencial de estudiante? (si/no): ").lower() == 'si'
Rango_vive_en_campus = input("¿a cuantos kilometros vive de la biblioteca? ") <= '3'
print("...................................")
#si tiene credencial de estudiante o vive a menos de 3 km de la biblioteca
puede_pedir_prestado = Credencial_estudiante or Rango_vive_en_campus
print(f"¿Puede pedir prestado el libro? {puede_pedir_prestado}")
print("...................................")