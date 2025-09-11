#1. Parentesis () : los que estan dentro de los parentesis se ejecutan primero
#2. Exponenciación ** : se ejecuta despues de los parentesis
#3. uniarios +, - : se ejecutan despues de la exponenciación
#4. Multiplicación *, División /, División entera //, Módulo % : se ejecutan despues de los unarios
#5. Suma +, Resta - : se ejecutan despues de la multiplicación y division
#6. Comparaciones <, >, <=, >=, ==, != : se ejecutan despues de las sumas y restas
#7. Operadores lógicos not, and, or : se ejecutan al final
#8. Asignación = : se ejecuta al final de todo
#De izquierda a derecha, excepto la exponenciación que es de derecha a izquierda

#Ejemplo de precedenciade operadores
resultado  = 12 / 3 + 2 * 3 - 1
print(f"rsultados: {resultado}")