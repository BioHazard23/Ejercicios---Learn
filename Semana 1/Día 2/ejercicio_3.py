#Lista vacia.

nombres = []

while True:
    nombre = input("Ingresa un nombre (o escribe 'salir' para terminar): ")
    if nombre.lower() == "salir":
        break
    nombres.append (nombre)

print ("Los nombres que hay en la lista son: ", nombres)