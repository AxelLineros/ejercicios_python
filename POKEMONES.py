nombre = ""
nivel = ""
tipo = 0
pokemon = input("ingrese el nombre del pokemon: ")
tipo = input("ingrese el tipo del pokemon: ")
nivel = int(input("ingrese el nivel del pokemon: "))

if(pokemon == "pichu" or pokemon == "pikachu" or pokemon == "raichu") and tipo == "electrico":
    if pokemon == "pichu":
        print("es nivel 1 a 15")
    elif "pikachu":
        print("es mivel de del 16 al 40")
    else:
        print("es nivel 41 a 100")
elif (pokemon == "charmander" or pokemon == "charmeleon" or pokemon == "charizard") and tipo == "fuego":
    if pokemon == "charmander":
        print("es nivel 1 a 15")
    elif "pikachu":
        print("es mivel de del 16 al 40")
    else:
        print("es nivel 41 a 100")


