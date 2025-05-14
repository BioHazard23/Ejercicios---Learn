#Menor de tres numeros.

num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))
num3 = int(input("Ingresa el tercer numero: "))

if num1 <= num2 and num1 <= num3:
    print (f"El numero mas pequeño es: {num1}")
elif num2 <= num1 and num2 <= num3:
    print (f"El numero mas pequeño es: {num2}")
else:
    print (f"El numero mas pequeño es: {num3}")