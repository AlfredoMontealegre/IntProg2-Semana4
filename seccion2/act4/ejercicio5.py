# Dado un total de cuenta y un porcentaje de propina (por ejemplo, 10%), calcula cuánto
# dejar de propina

total = int(input("Cuanto debes pagar el total?: "))
prop = int(input("Cuanto es el porcentaje de la propina?: "))

propina = ((prop * total)/100)

print(f"Usted debe pagar una propina de: ", propina)