#Gestion de biblioteca.

import time
biblioteca = {
    '001': {'Titulo': 'El principito', 'autor': 'Antoine de Saint-exupéry', 'Año': '1943'},
    '002': {'Titulo': 'Harry Potter y la piedra filosofal', 'Autor': 'J. K. Rowling', 'Año': '1997'}
}

def agregar ():
    id = input ("Ingresa ID: ")
    titulo = input ("Ingresa el titulo: ")
    autor = input ("Ingresa el autor: ")
    año = int(input ("Ingresa el año de publicacion: "))
    biblioteca[id] = {'Titulo': titulo, 'autor': autor, 'Año': año}
    time.sleep (1)
    print ("¡Tu libro se ha guardado con exito!")

def mostrar ():
    for id, datos in biblioteca.items():
        print(id, datos)

def buscar ():
    id = input ("Ingresa el ID del libro para buscar: ")
    if id in biblioteca:
        time.sleep (0.6)
        print ("Libro encontrado.")
        print (biblioteca[id])
    else:
        time.sleep (0.10)
        print ("Libro no encontrado.")

def modificar ():
    id = input ("Ingresa el ID a actualizar: ")
    if id in biblioteca:
        autor = input ("Ingresa el autor: ")
        año = int(input ("Ingresa el año: "))
        biblioteca[id]['autor'] = autor
        biblioteca[id]['año'] = año 
        time.sleep (1.1)
        print ("Libro actualizado.")

def eliminar ():
    id = input ("Ingresa el ID para eliminar")
    if id in biblioteca:
        del biblioteca[id]
        time.sleep (4)
        print ("Libro eliminado")
    else:
        time.sleep (0.6)
        print ("ID no encontrado")

while True:
    
    print ("\nSelecciona una de las siguientes opciones: ")
    time.sleep (1)
    print ("\n1. Agregar\n2. Mostrar\n3. Buscar\n4. Modificar\n5. Eliminar\n6. Salir ")
    opcion = input ("\nOpcion: ")
    #
    if opcion == '1':
        agregar()
    elif opcion == '2':
        mostrar()
    elif opcion == '3':
        buscar()
    elif opcion == '4':
        modificar()
    elif opcion == '5':
        eliminar()
    elif opcion == '6':
        print ("Hasta pronto.")
        break
    else:
        print("Opcion invalida")