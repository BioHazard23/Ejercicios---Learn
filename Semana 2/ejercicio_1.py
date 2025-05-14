#✈️ Sistema de Gestión y Costeo de Equipaje Aéreo

compras = []
contador_compras = 1

#Precios base
precios_base = {
    "nacional": 230000,
    "internacional": 4200000
}

#Se genera un ID unico
def general_id():
    global contador_compras
    id_compras = f"COMP{contador_compras:04d}"
    contador_compras += 1
    return id_compras

#Calcular el costo del equipaje
def calcular_costo_equipaje(peso):
    if peso <= 20:
        return 50000
    elif peso <= 30:
        return 70000
    elif peso <= 50:
        return 110000
    else:
        return None

#Registrar compra
def registrar_compra():
    nombre = input("Nombre del pasajero: ").lower()
    tipo_viaje = input("Tipo de viaje (Internacional/Nacional): ").lower()
    destino = "Bogota -> Medellin" if tipo_viaje == "Nacional" else "Bogota -> España"
    fecha = input("Fecha del viaje (YYYY/MM/DD): ")

    #Equipaje principal
    peso_principal = float(input("Peso del equipaje principal (kg): "))
    estado_principal = "Admitido"
    costo_equipaje = calcular_costo_equipaje(peso_principal)

    if costo_equipaje is None:
        estado_principal = "No admitido"
        costo_equipaje = 0

    #Equipaje de mano
    lleva_mano = input("¿Llevas equipaje de mano? (si/no): ").lower()
    estado_mano = "No aplica"
    if lleva_mano == "si":
        peso_mano = float(input("Peso del equipaje de mano (kg): "))
        estado_mano = "Admitido" if peso_mano <= 13 else "Rechazado"
    
    #Calcular total
    precio_base = precios_base.get(tipo_viaje, 0)
    total = precio_base + costo_equipaje

    id_compra = general_id()

    compra = {
        "ID": id_compra,
        "Nombre": nombre, 
        "Destino": destino, 
        "Fecha": fecha, 
        "Estado Principal": estado_principal, 
        "Estado Mano": estado_mano,
        "Total": total,
        "Tipo": tipo_viaje
    }

    compras.append(compra)

    #Mostrar resumen
    print("\n---------- Resumen de la compra ----------")
    print(f"\nID de compra: {id_compra}")
    print(f"\nNombre: {nombre}")
    print(f"\nDestino: {destino}")
    print(f"\nFecha: {fecha}")
    print(f"\nEstado del equipaje principal: {estado_principal}")
    print(f"\nEstado del equipaje de mano: {estado_mano}")
    print(f"\nCosto total del viaje: ${total:,}\n")

#Reporte para el admin
def reporte_total_recaudado():
    total = sum(c["Total"] for c in compras)
    print(f"Total recaudado en todas las compras: ${total:,}")

def reporte_por_fecha():
    fecha = input("Ingrese la fecha (YYYY/MM/DD): ")
    total = sum(c["Total"] for c in compras if c["Fecha"] == fecha)
    print(f"Total recaudado el {fecha}: ${total:,}")

def reporte_numero_pasajeros():
    print(f"El numero de pasajeros procesados es: {len(compras)}")

def reporte_por_tipo():
    nacionales = sum(1 for c in compras if c["Tipo"] == "nacional")
    internacionales = sum(1 for c in compras if c["Tipo"] == "internacional")
    print(f"Pasajeros Nacionales: {nacionales}")
    print(f"Pasajeros Internacionales: {internacionales}")    

def buscar_compra_por_id():
    id_busqueda = input("Ingrese el ID de la compra: ").upper()
    for c in compras:
        if c["ID"] == id_busqueda:
            print("\n---------- Detalle de la compra ----------")
            for clave, valor in c.items():
                print(f"{clave}: {valor}")
            return
    print("Compra no encontrada")

def menu():
    while True:
        print("\n---------- Sistema de Gestión de Equipaje Aéreo ----------")
        print("\n1.) Registrar nueva compra.")
        print("\n2.) Reporte: Total recaudado.")
        print("\n3.) Reporte: Total por fecha.")
        print("\n4.) Reporte: Numero de pasajeros.")
        print("\n5.) Reporte: Nacionales / Internacionales.")
        print("\n6.) Buscar compra por ID.")
        print("\n7.) Salir.")

        opcion = input("\nSelecciona una opcion (1-7): ")

        if opcion == "1":
            registrar_compra()
        elif opcion == "2":
            reporte_total_recaudado() 
        elif opcion == "3":
            reporte_por_fecha
        elif opcion == "4":
            reporte_numero_pasajeros()
        elif opcion == "5":
            reporte_por_tipo()
        elif opcion == "6":
            buscar_compra_por_id()
        elif opcion == "7":
            print("Saliendo del programa.")
            print("--- ¡Hasta Luego! ---")
            break
        else:
            print("Opcion invalida.")

#Ejecuta el menu
menu()




