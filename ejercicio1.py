not1 = float(input("Ingrese la nota 1 (30%): "))
not2 = float(input("Ingrese la nota 2 (40%): "))
not3 = float(input("Ingrese la nota 3 (30%): "))

promedioPresentacion = (not1 * 0.3) + (not2 * 0.4) + (not3 * 0.3)

print("Su promedio de presentación es: ",promedioPresentacion)

notEX = float(input("Ingrese la nota de su examen: "))

promedioFINAL = (promedioPresentacion * 0.6) + (notEX * 0.4)

print("Su promedio final de la asignatura es: ", promedioFINAL )