# Diseñe un algoritmo que lea los datos necesarios y calcule la masa, según la formula

print(f"Vamos a calcular la masa de un objeto")
presion = int(input("Agrege la presion calculada: "))
volumen = int(input("Agrege el volumen calculado: "))
temperatura = int(input("Agrege la temperatura calculada: "))

masa = (presion * volumen)/((0.37 * (temperatura + 460)))

print(f"La masa calculada es de: ", masa)