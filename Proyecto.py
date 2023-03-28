#Aqui voy a crear unas listas donde puedo almacenar las bibliotecas de cada cliente, empleado, servicio

clientes = []
empleados = []
servicios_brindados = []

#Creamos el menu principal
while True:
    
    print("---Menu Principal---")
    print("1. Empleados")
    print("2. Clientes")
    print("3. Trabajos")
    print("4. Salir")
    
    opcion = input("Ingrese su opción: ")

#Aqui estan todos los sub menus
    #Codigo de Empleados
    if opcion == "1":
        while True:
            print("1. Ingresar empleado")
            print("2. Borrar empleado")
            print("3. Ver empleados")
            print("4. Volver")

            opcion_sub = input("Ingrese su opción: ")

            if opcion_sub == "1":
                #Agregamos empleados en diccionarios
                empleado = {}
                empleado['nombre'] = input("Ingrese el nombre del empleado: ")
                empleado['especialidad'] = input("Ingrese la especialidad del empleado: ")
                empleado['sexo'] = input("Ingrese el sexo del empleado: ")
                
                #Verificar si ya existe el empleado
                encontrado = False
                for e in empleados:
                    if e['nombre'] == empleado['nombre']:
                        encontrado = True
                        break
                    
                if encontrado:
                    print("El empleado ya existe.")
                else:
                    #Buscar la posición para insertar el nuevo empleado manteniendo el orden
                    posicion = 0
                    for e in empleados:
                        if e['nombre'] > empleado['nombre']:
                            break
                        posicion += 1
                        
                    #Insertar el nuevo empleado en la posición correspondiente
                    empleados.insert(posicion, empleado)
                    print("Empleado agregado correctamente.")
            #funcion para borrar un empledo
            elif opcion_sub == "2":
                id_empleado = input("Ingrese el nombre del empleado a borrar: ")
                encontrado = False
                for e in empleados:
                    if e['nombre'] == id_empleado:
                        encontrado = True
                        empleados.remove(e)
                        print("Empleado borrado correctamente.")
                        break
                if not encontrado:
                    print("Empleado no encontrado.")
            #funcion para visualizar todos los usuarios que existan
            elif opcion_sub == "3":
                if len(empleados) == 0:
                    print("No hay empleados.")
                else:
                    for e in empleados:
                        print(f"Nombre: {e['nombre']}")
                        print(f"Especialidad: {e['especialidad']}")
                        print(f"Sexo: {e['sexo']}")
                        print()
            elif opcion_sub == "4":
                break 
            else:
                print("Opción no válida")
    #codigo de clientes
    elif opcion == "2":
        while True:
            print("1. Ingresar cliente")
            print("2. modificar cliente")
            print("3. Ver clientes")
            print("4. Volver")

            opcion_sub = input("Ingrese su opción: ")
            #ingresamos los datos de los clientes
            if opcion_sub == "1":
                cliente = {}
                cliente['nombre'] = input("Ingrese el nombre del cliente: ")
                cliente['cedula'] = input("Ingrese la cedula del cliente: ")
                cliente['telefono'] = input("Ingrese el telefono del cliente: ")
                    
                #Buscar la posición para insertar el nuevo cliente manteniendo el orden
                posicion = 0
                for c in clientes:
                    if c['cedula'] > cliente['cedula']:
                        break
                    posicion += 1
                    
                #Insertar el nuevo cliente en la posición correspondiente
                clientes.insert(posicion, cliente)
                print("Cliente agregado correctamente.")
            #Modificar datos de los clientes 
            elif opcion_sub == "2":
                nombre = input("Ingrese el nombre del cliente que desea modificar: ")
                encontrado = False
                for c in clientes:
                    if c['nombre'] == nombre:
                        encontrado = True
                        c['cedula'] = input("Ingrese la nueva cedula del cliente: ")
                        c['telefono'] = input("Ingrese el nuevo telefono del cliente: ")
                        print("Cliente modificado correctamente.")
                        break
                if not encontrado:
                    print("Cliente no encontrado.")
            #Ver los clientes en el sistema
            elif opcion_sub == "3":
                if len(clientes) == 0:
                    print("No hay clientes.")
                else:
                    for c in clientes:
                        print(f"Nombre: {c['nombre']}")
                        print(f"Cedula: {c['cedula']}")
                        print(f"Telefono: {c['telefono']}")
                        print()

            elif opcion_sub == "4":
                break 
            else:
                print("Opción no válida")
    #Codigo de trabajos
    elif opcion == "3":
        while True:
            print("1. Brindar un servicio")
            print("2. Ver servicios brimdados")
            print("3. Empleado disponible")
            print("4. Volver")

            opcion_sub = input("Ingrese su opción: ")

            if opcion_sub == "1":
                print("Empleados disponibles:")
                for i, e in enumerate(empleados):
                    print(f"{i+1}. {e['nombre']} - {e['especialidad']}")
                
                #Seleccionar el empleado para brindar el servicio
                empleado = None
                while not empleado:
                    opcion_empleado = input("Seleccione el empleado (Ingrese el número): ")
                    if opcion_empleado.isdigit() and int(opcion_empleado) in range(1, len(empleados)+1):
                        empleado = empleados[int(opcion_empleado)-1]
                    else:
                        print("Opción no válida. Intente de nuevo.")

                # Agregar el servicio a la lista de servicios brindados
                servicio = {}
                servicio['cliente'] = input("Ingrese el nombre del cliente: ")
                servicio['servicio'] = input("Ingrese el servicio: ")
                servicio['empleado'] = empleado['nombre']
                servicios_brindados.append(servicio)
                print("Servicio agregado correctamente.")
            #Ver los servicios brindados
            elif opcion_sub == "2":
                if len(servicios_brindados) == 0:
                    print("No hay servicios brindados.")
                else:
                    for s in servicios_brindados:
                        print(f"Cliente: {s['cliente']}")
                        print(f"Servicio: {s['servicio']}")
                        print(f"Empleado: {s['empleado']}")
                        print()
            #Ver los empleados disponibles
            elif opcion_sub == "3":
                if len(empleados) == 0:
                    print("No hay empleados.")
                else:
                    disponibles = []
                    for e in empleados:
                        encontrado = False
                        for s in servicios_brindados:
                            if s['empleado'] == e['nombre']:
                                encontrado = True
                                break
                        if not encontrado:
                            disponibles.append(e)
                    
                    if len(disponibles) == 0:
                        print("No hay empleados disponibles.")
                    else:
                        print("Empleados disponibles:")
                        for i, e in enumerate(disponibles):
                            print(f"{i+1}. {e['nombre']} - {e['especialidad']}")
            elif opcion_sub == "4":
                break 
            else:
                print("Opción no válida")

    elif opcion == "4":
        break  #Sale del bucle del menú principal

    else:
        print("Opción no válida")
