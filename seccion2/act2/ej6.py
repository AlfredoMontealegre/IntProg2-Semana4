# Crea un algoritmo que, dado el año de nacimiento de una persona y el año actual,
# su edad actual y su edad en 10 años.

edad_ac = 2025
edad_per = int(input("Agrege el año de su nacimiento: "))

edad_real = edad_ac - edad_per
edad_futu = edad_real + 10

print(f"Año actual: ", edad_ac)
print(f"Edad: ", edad_real)
print(f"Edad dentro de 10 años: ", edad_futu)