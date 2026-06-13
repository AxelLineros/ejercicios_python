# ---------------------------------------------------------------------
# 1. Acceso por clave []
# Problema: Determina qué estudiantes tienen promedio superior a 5.0.
print("--- 1. Acceso por clave [] ---")
promedios = {
    "Ana": 6.1,
    "Luis": 4.8,
    "Camila": 5.7,
    "Pedro": 3.9
}

for estudiante in promedios:
    if promedios[estudiante] > 5.0:
        print(f"Estudiante con promedio superior a 5.0: {estudiante} ({promedios[estudiante]})")

print("\n" + "-"*40 + "\n")


# ---------------------------------------------------------------------
# 2. Método keys()
# Problema: Mostrar todas las asignaturas del siguiente diccionario.

print("--- 2. Método keys() ---")
asignaturas = {
    "MAT100": "Matemática",
    "PRO101": "Programación",
    "RED201": "Redes",
    "BD301": "Base de Datos"
}

print("Códigos de las asignaturas:")
for codigo in asignaturas.keys():
    print("-", codigo)

print("\n" + "-"*40 + "\n")


# ---------------------------------------------------------------------
# 3. Método values()
# Problema: Mostrar todas las temperaturas superiores a 25 grados.
print("--- 3. Método values() ---")
temperaturas = {
    "Lunes": 22,
    "Martes": 28,
    "Miércoles": 30,
    "Jueves": 21,
    "Viernes": 26
}

print("Temperaturas superiores a 25°C:")
for temp in temperaturas.values():
    if temp > 25:
        print(f"- {temp}°C")

print("\n" + "-"*40 + "\n")


# ---------------------------------------------------------------------
# 4. Método items()
# Problema: Mostrar los alumnos aprobados (se asume aprobación con nota >= 4.0).

print("--- 4. Método items() ---")
notas = {
    "Ana": 5.5,
    "Luis": 3.8,
    "Pedro": 4.7,
    "Camila": 6.2
}

print("Alumnos aprobados:")
for alumno, nota in notas.items():
    if nota >= 4.0:
        print(f"- {alumno}: {nota}")

print("\n" + "-"*40 + "\n")


# ---------------------------------------------------------------------
# 5. Método get()
# Problema: Busca el producto "impresora" utilizando get().

print("--- 5. Método get() ---")
catalogo = {
    "mouse": 12000,
    "teclado": 18000,
    "monitor": 150000
}

buscar = "impresora"
precio = catalogo.get(buscar)

if precio:
    print(f"El precio de '{buscar}' es: ${precio}")
else:
    print(f"El producto '{buscar}' no se encuentra en el catálogo.")

print("\n" + "-"*40 + "\n")


# ---------------------------------------------------------------------
# 6. Función len()
# Problema: Determina cuántos productos tiene el inventario.

print("--- 6. Función len() ---")
inventario = {
    "Mouse": 20,
    "Teclado": 15,
    "Monitor": 5,
    "Webcam": 12,
    "Audífonos": 9
}

total_productos = len(inventario)
print("Cantidad total de productos en el inventario:", total_productos)

print("\n" + "-"*40 + "\n")


# ---------------------------------------------------------------------
# Desafío Integrador
# ---------------------------------------------------------------------
print("--- DESAFÍO INTEGRADOR ---")
ventas = {
    "Mouse": 15,
    "Teclado": 8,
    "Monitor": 3,
    "Webcam": 11,
    "Audífonos": 5
}

# 1. Mostrar todos los productos y cantidades usando items().
print("1. Inventario completo (Producto - Cantidad):")
for producto, cantidad in ventas.items():
    print(f"   {producto}: {cantidad} unidades")

print()

# 2. Detectar cuáles tienen stock menor a 10.
print("2. Alerta de stock crítico (menor a 10 unidades):")
for producto, cantidad in ventas.items():
    if cantidad < 10:
        print(f"   ¡Atención! {producto} tiene stock bajo ({cantidad})")

print()

# 3. Contar cuántos productos existen usando len().
print("3. Conteo total de productos:")
print(f"   Hay un total de {len(ventas)} tipos de productos diferentes.")

print()

# 4. Mostrar únicamente las cantidades usando values().
print("4. Lista de todas las cantidades en stock:")
for cantidad in ventas.values():
    print(f"   - {cantidad}")

print()

# 5. Mostrar únicamente los nombres usando keys().
print("5. Lista de todos los nombres de productos:")
for producto in ventas.keys():
    print(f"   - {producto}")