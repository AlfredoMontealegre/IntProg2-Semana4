# Algoritmo para calcular el porcentaje de mujeres y varones en un aula

mujeres = int(input("Ingrese cantidad de mujeres: "))
hombres = int(input("Ingrese cantidad de hombres: "))

total = hombres + mujeres

per_mujeres = mujeres / total
per_hombres = hombres / total

print(f"Hay un porcentaje de mujeres de: ", per_mujeres)
print(f"Hay un porcentaje de hombres de: ", per_hombres)