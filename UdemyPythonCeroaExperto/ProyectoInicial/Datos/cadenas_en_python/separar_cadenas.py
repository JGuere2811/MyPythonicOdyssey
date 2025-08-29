import re

datos = "Juan; 72046745, 935148362, av.los girazoles lt 13, 30 / Mexico\\ sobrecalentamiento"
# Reemplaza la barra invertida por barra normal para simplificar
datos = datos.replace("\\", "/")
# Expresión regular para separar por doble espacio o cualquiera de los símbolos (sin el punto)
partes = re.split(r' {2,}|/|,|;|\||-|_', datos)
campos = [parte.strip() for parte in partes if parte.strip()]
print(campos)