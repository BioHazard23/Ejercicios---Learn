#Adivina el numero.

numero_secreto = 7

adivina = int(input("intenta adivinar el numero del 1 al 10: "))

if adivina == numero_secreto:
    print ("¡Adivinaste el numero!")
elif adivina > numero_secreto:
    print ("Intenta con un numero menor al que ingresaste.")
else:
    print ("Intenta con un numero mayor al que ingresaste.")