pares = 0
impares = 0
sumaTotal = 0

for i in range(3):
    num = int(input("Ingrese numero: "))
    sumaTotal += num

    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Se ingresaron", pares ,"números pares.")
print("Se ingresaron", impares ,"números impares.")

if sumaTotal > 100:
    print("La suma es mayor a 100")
else:
    print("La suma no es mayor a 100")

if sumaTotal % 2 == 0:
    print("La suma es par")
else:
    print("La suma es impar")