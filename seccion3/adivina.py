#Adivinar un Numero
import random

numero_secreto = random.randint(1,10)
while(True)
    numero_user = int(input("Dime un numero del 1-10: "))
    print("El numero era:", numero_secreto)
     if(numero_secreto == numero_user):
        print("Felicidades, te ganaste 10 puntos extras")
        break
    else:
        print("Lo siento, tenes que invitar a un churro a todos")
    if(numero_user > numero_secreto):
        print("El numero es menor")
    else
        print("El numero es mayor")