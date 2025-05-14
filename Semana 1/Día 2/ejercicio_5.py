#¿Esta en la lista de invitados?

lista = ["juan", "salome", "yeniffer", "wilson"]

nombre = input("Dame por favor tu nombre: ").lower()

if nombre in lista:
    print ("Estas en la lista de invitados.")
else:
    print ("No estas invitado.")