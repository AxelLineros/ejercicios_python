opcion = 1
pokemon = ""
tipo = ""

while opcion == 1:
    pokemon = input("ingrese el pokemon: ")
    tipo = input("ingrese el tipo del pokemon: ")

    if(pokemon == "pichu" or pokemon == "pikachu" or pokemon == "raichu") and tipo == "electrico":
        if pokemon == "pichu":
            print("el nivel del pokemon es 1 - 15")
        elif pokemon == "pikachu":
            print("el nivel del pokemon es 16 - 40")
        else:
            print("el nivel del pokemon es 41 - 100")

    elif(pokemon == "charmander" or pokemon == "charmeleon" or pokemon == "charizard") and tipo == "fuego":
        if pokemon == "charmander":
            print("el nivel del pokemon es 1 - 15")
        elif pokemon == "charmeleon":
            print("el nivel del pokemon es 16 - 40")
        else:
            print("el nivel del pokemon es 41 - 100")

    elif(pokemon == "bulbasour" or pokemon == "ivysour" or pokemon == "venusour") and tipo == "planta":
        if pokemon == "bulbasour":
            print("el nivel del pokemon es 1 - 15")
        elif pokemon == "ivysour":
            print("el nivel del pokemon es 16 - 40")
        else:
            print("el nivel del pokemon es 41 - 100")
    else:
        print("no corresponde al pokemon")
print("desea continuar? "SI/NO, opcion)
