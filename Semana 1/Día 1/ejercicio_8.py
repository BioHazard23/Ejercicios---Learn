#Clasificacion de IMC.

peso = float(input("Ingresa tu peso en Kg: "))
altura = float(input("Ingresa tu altura en metros: "))

imc = peso / (altura**2)

print (f"Tu IMC es: {imc:.2f}")

if imc < 18.5:
    print ("Bajo de peso.")
elif 18.5 <= imc <= 24.9:
    print ("Normal.")
elif 25 <= imc <= 29.9:
    print ("Sobrepeso.")
else:
    print ("Obesidad")