# Algoritmo que calcule el porcentaje de un número dado.

print("Calculadora de Porcentaje")
num = int(input("Ingrese un numero: "))
porc = int(input("Que porcentaje quieres conocer?: "))

res = (num * porc)/100

print(f"El porcentaje es del: ", res)