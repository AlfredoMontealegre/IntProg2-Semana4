# Pide una edad actual y muestra qué edad tendrá el usuario dentro de 5, 10 y 20 años.

edad_real = int(input("Agrege su edad: "))

edad_futu = edad_real + 10
edad_futu2 = edad_real + 5
edad_futu3 = edad_real + 20

print(f"Edad: ", edad_real)
print(f"Edad dentro de 5 años: ", edad_futu2)
print(f"Edad dentro de 10 años: ", edad_futu)
print(f"Edad dentro de 20 años: ", edad_futu3)