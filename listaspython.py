# =====================================================================
# Listas en Python: Funciones y Métodos Básicos - SOLUCIONES
# =====================================================================

# ---------------------------------------------------------------------
# 1. Método append()
# Problema: Crear una lista con edades mayores o iguales a 18.
# ---------------------------------------------------------------------
print("--- 1. Método append() ---")
edades = [12, 18, 25, 15, 30, 17, 20]
mayores_edad = []

for edad in edades:
    if edad >= 18:
        mayores_edad.append(edad)

print("Mayores de edad:", mayores_edad)
print("\n" + "-"*40 + "\n")


# ---------------------------------------------------------------------
# 2. Método insert()
# Problema: Insertar al inicio ("prioridad") o al final ("normal").
# ---------------------------------------------------------------------
print("--- 2. Método insert() ---")
estudiantes = ["Ana", "Luis", "Pedro", "Camila"]
nuevos = ["prioridad: Sofía", "normal: Diego", "prioridad: Mateo"]

for estudiante in nuevos:
    if "prioridad" in estudiante:
        estudiantes.insert(0, estudiante)
    else:
        estudiantes.append(estudiante)

print("Lista final de estudiantes:")
for estudiante in estudiantes:
    print("-", estudiante)

print("\n" + "-"*40 + "\n")


# ---------------------------------------------------------------------
# 3. Método remove()
# Problema: Eliminar de inscritos a quienes cancelaron el taller.
# ---------------------------------------------------------------------
print("--- 3. Método remove() ---")
inscritos = ["Ana", "Luis", "Pedro", "Camila", "Diego"]
cancelados = ["Pedro", "Sofía", "Diego"]

for nombre in cancelados:
    if nombre in inscritos:
        inscritos.remove(nombre)
        print("Cancelado eliminado:", nombre)
    else:
        print("No estaba inscrito:", nombre)

print("Lista actualizada de inscritos:", inscritos)
print("\n" + "-"*40 + "\n")


# ---------------------------------------------------------------------
# 4. Método pop()
# Problema: Atender a los clientes uno por uno hasta vaciar la fila.
# ---------------------------------------------------------------------
print("--- 4. Método pop() ---")
fila = ["Cliente 1", "Cliente 2", "Cliente 3", "Cliente 4"]

while len(fila) > 0:
    cliente = fila.pop(0)
    print("Cliente atendido:", cliente)
    print("Fila actual:", fila)

print("\n" + "-"*40 + "\n")


# ---------------------------------------------------------------------
# 5. Método sort()
# Problema: Filtrar precios >= 10000 y ordenarlos de menor a mayor.
# ---------------------------------------------------------------------
print("--- 5. Método sort() ---")
precios = [12990, 4990, 18990, 2990, 9990, 15990]
precios_altos = []

for precio in precios:
    if precio >= 10000:
        precios_altos.append(precio)

precios_altos.sort()

print("Precios altos ordenados:", precios_altos)
print("\n" + "-"*40 + "\n")


# ---------------------------------------------------------------------
# 6. Función len()
# Problema: Separar temperaturas altas/bajas y comparar qué días hubo más.
# ---------------------------------------------------------------------
print("--- 6. Función len() ---")
temperaturas = [12, 18, 25, 30, 15, 28, 10]
temperaturas_altas = []
temperaturas_bajas = []

for temperatura in temperaturas:
    if temperatura >= 25:
        temperaturas_altas.append(temperatura)  # Nota: Corregido error de tipografía del original
    else:
        temperaturas_bajas.append(temperatura)

print("Total de temperaturas:", len(temperaturas))
print("Temperaturas altas:", len(temperaturas_altas))
print("Temperaturas bajas:", len(temperaturas_bajas))

if len(temperaturas_altas) > len(temperaturas_bajas):
    print("Hubo más días cálidos.")
else:
    print("Hubo más días fríos o la misma cantidad.")

print("\n" + "-"*40 + "\n")


# ---------------------------------------------------------------------
# Desafío Integrador Final
# Contexto: Filtrar productos únicos de las ventas del día y ordenarlos.
# ---------------------------------------------------------------------
print("--- DESAFÍO INTEGRADOR FINAL ---")
ventas = ["mouse", "teclado", "mouse", "monitor", "webcam", "mouse", "teclado", "audífonos"]
productos_unicos = []

for producto in ventas:
    if producto not in productos_unicos:
        productos_unicos.append(producto)

productos_unicos.sort()

print("Cantidad de productos distintos vendidos:", len(productos_unicos))
print("Productos distintos ordenados:", productos_unicos)