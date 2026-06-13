contraseña = input("ingrese contraseña: ")
largo = len(contraseña)
especiales = "-_*.!?#%"

Numero = False
Letras = False
Espacios = False
EspecialesTOT = 0

for Car in contraseña:
    if "0" <= Car <= "9":
        Numero = True
    if "a" <= Car <= "z" or "A" <= Car <= "Z":
        Letras = True
    if Car == " ":
        Espacios = True
    if Car in especiales:
        EspecialesTOT += 1

FinMal = largo > 0 and contraseña[-1] in especiales

if (8 <= largo <= 16) and Numero and Letras and not Espacios and EspecialesTOT <= 1 and not FinMal:
    print("contraseña valida")
else:
    print("contraseña invalida")