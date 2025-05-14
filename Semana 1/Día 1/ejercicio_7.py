#Mayor de dos numeros.

num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))

if num1 > num2:
    print (f"el numero mayor es: {num1}")
elif num1 < num2:
    print (f"el numero mayor es: {num2}")
else:
    print ("Ambos numeros son iguales")