# 15. Algoritmo que calcule el salario de un trabajador de la manera siguiente. El trabajador
# cobra un precio fijo por hora y se le descuento el 5% en concepto de impuesto sobre la
# renta. El programa debe pedir el nombre del trabajador, las horas trabajadas y el precio
# que cobra por hora. Como salida debe imprimir el nombre del trabajador, el sueldo bruto,
# el descuento de renta y el salario a paga.

nombre = str(input("Ingrese su nombre: "))
horas_trb = int(input("Ingrese sus horas trabajadas: "))
sueldo_hora = int(input("Ingrese el precio por hora de su trabajo: "))

sueldo = horas_trb * sueldo_hora
descuento = sueldo * 0.05

sueldo_final = sueldo - descuento

print(f"="*20)
print(f"Nombre del Trabajador: ", nombre)
print(f"Salario Bruto: ", sueldo)
print(f"Descuento de Renta: ", descuento)
print(f"Salario Final: ", sueldo_final)
print(f"="*20)