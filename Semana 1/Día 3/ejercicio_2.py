#Agenda de contactos.
 
import time
agenda = {}

def agregar ():
    nombre = input ("Ingresa el nombre del contacto: ")
    if nombre.lower() in agenda:
        print ("Ese contacto ya se encuentra guardado.")
        return
    telefono = int(input("Ingresa el numero de telefono: "))
    email = input ("Ingresa el email: ")
    agenda [nombre] = {'tel': telefono, 'email': email}
    print ("\nContacto guardado.")

def mostrar ():
    for nombre, datos in agenda.items():
        print (nombre, datos)

def buscar ():
    nombre = input ("Ingresa el nombre que quisieras buscar: ")
    if nombre in agenda:
        print (agenda[nombre])
    else:
        print ("Nombre no encontrado.")

def actualizar ():
    nombre = input ("Ingresa el nombre del contacto que quisieras actualizar: ")
    if nombre in agenda:
        telefono = input("Ingresa el nuevo telefono: ")
        email = input ("Ingresa el nuevo email: ")
        if telefono:
            agenda[nombre]['tel'] = telefono
        if email:
            agenda[nombre]['email'] = email
        print ("El contacto se ha actualizado.")
    else:
        print ("El contacto no se encuentra guardado.")

def eliminar ():
    nombre = input ("Ingresa el nombre del contacto que quisieras eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print ("El contacto se ha eliminado.")
    else:
        print ("El contacto ingresado no existe.")

while True:
    print ("Selecciona una de las siguientes opciones: ")
    print ("\n1. Agregar\n2. Mostrar\n3. Buscar\n4. Actualizar\n5. Eliminar\n6. Salir ")
    opcion = input ("\nOpcion: ")
    if opcion == '1':
        agregar()
    elif opcion == '2':
        mostrar()
    elif opcion == '3':
        buscar()
    elif opcion == '4':
        actualizar()
    elif opcion == '5':
        eliminar()
    elif opcion == '6':
        print ("Hasta pronto.")
        break
    else:
        print("Opcion invalida")