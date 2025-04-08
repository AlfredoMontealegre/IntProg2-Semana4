# Calcular el número de pulsaciones que una persona debe tener por cada 10 segundos
# de ejercicio, si la fórmula

print("Calcularemos el numero de pulsaciones")
edad = int(input("Ingrese su edad: "))

n_pulsaciones = (200 - edad)/10

print(f"El numero de pulsaciones c/10s que deberias tener para tu edad es de: ", n_pulsaciones)