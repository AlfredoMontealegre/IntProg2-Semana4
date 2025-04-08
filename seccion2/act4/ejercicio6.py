# Solicita el precio de 3 productos y muestra:
# Subtotal
# IVA (15%)
# Total a pagar

prod1 = int(input("Ingrese el valor del primer producto: "))
prod2 = int(input("Ingrese el valor del segundo producto: "))
prod3 = int(input("Ingrese el valor del tercer producto: "))

subtotal = prod1+prod2+prod3
iva = subtotal * 0.15
total = subtotal + iva

print(f"Subtotal: ", subtotal)
print(f"IVA: ", iva)
print(f"Total: ", total)
