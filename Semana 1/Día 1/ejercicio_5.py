#Calculadora de propinas.

total = float(input("Ingresa el total de la cuenta: "))
porcentaje = int(input("Cual es el porcentaje de propina que quisieras dar: "))

propina = total * porcentaje / 100

print(f"la propina es de: ${propina:.2f}")
