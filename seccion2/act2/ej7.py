# Diseña un algoritmo que intercambie el valor de dos variables numéricas. Usa una
# variable auxiliar para hacerlo.

b = 2
a = 4

temp = b
tempb = a
a = tempb
b = temp

print(f"El valor de A ahora es: ", temp)
print(f"El valor de B ahora es: ", tempb)