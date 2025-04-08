# Calcular el nuevo salario de un empleado si obtuvo un incremento del 8% sobre su
# salario actual y un descuento de 2,5% por servicios.

salario = int(input("Ingrese su salario: "))
incremento = salario * 0.08
descuento = salario * 0.25

salario_new = salario + incremento + descuento

print(f"Se incremento un: ", incremento)
print(f"Descuento: ", descuento)
print(f"Tu salario nuevo es: ", salario_new)