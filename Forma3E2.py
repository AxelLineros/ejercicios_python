nombres = []
edades = []

while True:
    print("1.- Ingresar usuario y edad.")
    print("2.- Calcular edad promedio.")
    print("3.- Salir.")
    
    opcion = input("Seleccione opción: ")
    
    if opcion == "1":
        if len(nombres) >= 3:
            print("No se permiten más ingresos.")
        else:
            nombre = input("Ingrese nombre de usuario: ")
            while True:
                try:
                    edad = int(input("Ingrese edad del usuario: "))
                    break  
                except ValueError:
                    print("Error: La edad debe ser un número entero.")
            nombres.append(nombre)
            edades.append(edad)
            print(f"Usuario {nombre} registrado con éxito.")
            
    elif opcion == "2":
        Usuarios = len(edades)
        
        if Usuarios == 0:
            print("No es posible calcular promedio (no hay usuarios ingresados).")
        else:
            SumaEdades = sum(edades)
            promedio = SumaEdades / Usuarios
            print(f"La edad promedio de los {Usuarios} usuarios ingresados es: {promedio:.1f} años.")
            
    elif opcion == "3":
        print("Saliendo del programa. ¡Hasta luego!")   
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 3.")