from modelos import PokemonAgua, PokemonFuego, PokemonElectrico, PokemonHierba


def _obtener_tipo_string(pokemon):
    if isinstance(pokemon, PokemonAgua):
        return "Agua"
    elif isinstance(pokemon, PokemonFuego):
        return "Fuego"
    elif isinstance(pokemon, PokemonElectrico):
        return "Electrico"
    else:
        return "Hierba"


def elegir_pokemon():
    print("\nElige tu Pokemon de inicio:")
    print("1. Agua      - Squirtle  (Squirtle -> Wartortle -> Blastoise)")
    print("2. Fuego     - Charmander (Charmander -> Charmeleon -> Charizard)")
    print("3. Electrico - Pichu      (Pichu -> Pikachu -> Raichu)")
    print("4. Hierba    - Bulbasaur  (Bulbasaur -> Ivysaur -> Venusaur)")

    while True:
        try:
            opcion = input("Elige (1-4): ").strip()
            if opcion == "1":
                return PokemonAgua()
            elif opcion == "2":
                return PokemonFuego()
            elif opcion == "3":
                return PokemonElectrico()
            elif opcion == "4":
                return PokemonHierba()
            else:
                print("Opcion invalida, intenta de nuevo.")
        except ValueError:
            print("Error: debes ingresar una opcion valida.")


def crear_enemigos_iniciales():
    enemigo1 = PokemonFuego()
    enemigo1.nombre = "Arcanine"
    enemigo1.descripcion = "Pokemon Fuego muy poderoso"
    enemigo1.ataque = 110
    enemigo1.defensa = 80
    enemigo1.vida = 200
    enemigo1.ataque_especial = "Lanzallamas"

    enemigo2 = PokemonAgua()
    enemigo2.nombre = "Gyarados"
    enemigo2.descripcion = "Pokemon Agua salvaje y feroz"
    enemigo2.ataque = 125
    enemigo2.defensa = 79
    enemigo2.vida = 190
    enemigo2.ataque_especial = "Hidrobomba"

    enemigo3 = PokemonHierba()
    enemigo3.nombre = "Caterpie"
    enemigo3.descripcion = "Pokemon Hierba muy debil"
    enemigo3.ataque = 15
    enemigo3.defensa = 10
    enemigo3.vida = 40
    enemigo3.ataque_especial = "Latigo Cepa"

    enemigo4 = PokemonElectrico()
    enemigo4.nombre = "Magnemite"
    enemigo4.descripcion = "Pokemon Electrico pequeno y debil"
    enemigo4.ataque = 20
    enemigo4.defensa = 15
    enemigo4.vida = 35
    enemigo4.ataque_especial = "Impactrueno"

    return [enemigo1, enemigo2, enemigo3, enemigo4]


def crear_enemigo_personalizado(lista_enemigos):
    print("\n--- CREAR POKEMON ENEMIGO PERSONALIZADO ---")
    nombre = input("Nombre del Pokemon: ").strip()
    if not nombre:
        nombre = "Desconocido"
    descripcion = input("Descripcion: ").strip()
    if not descripcion:
        descripcion = "Sin descripcion"

    ataque = None
    while ataque is None:
        try:
            ataque = int(input("Ataque (1-1000): "))
        except ValueError:
            print("Error: debes ingresar un numero valido.")
            ataque = None

    defensa = None
    while defensa is None:
        try:
            defensa = int(input("Defensa (1-1000): "))
        except ValueError:
            print("Error: debes ingresar un numero valido.")
            defensa = None

    vida = None
    while vida is None:
        try:
            vida = int(input("Vida (1-1000): "))
        except ValueError:
            print("Error: debes ingresar un numero valido.")
            vida = None

    ataque_especial = input("Nombre del ataque especial: ").strip()
    if not ataque_especial:
        ataque_especial = "Ataque"

    print("\nElige el tipo:")
    print("1. Agua")
    print("2. Fuego")
    print("3. Electrico")
    print("4. Hierba")

    tipo = None
    while tipo is None:
        try:
            tipo = input("Tipo: ").strip()
            if tipo not in ["1", "2", "3", "4"]:
                print("Opcion invalida, intenta de nuevo.")
                tipo = None
        except ValueError:
            print("Error: debes ingresar una opcion valida.")
            tipo = None

    if tipo == "1":
        nuevo = PokemonAgua()
    elif tipo == "2":
        nuevo = PokemonFuego()
    elif tipo == "3":
        nuevo = PokemonElectrico()
    else:
        nuevo = PokemonHierba()

    nuevo.nombre = nombre
    nuevo.descripcion = descripcion
    nuevo.ataque = ataque
    nuevo.defensa = defensa
    nuevo.vida = vida
    nuevo.ataque_especial = ataque_especial

    lista_enemigos.append(nuevo)
    print(f"\n{nombre} fue agregado a la lista de enemigos!\n")


def pruebas_manejo_errores():
    while True:
        print("\n========================================")
        print("    PRUEBAS DE MANEJO DE ERRORES")
        print("========================================")
        print("1. ValueError        - dato numerico invalido")
        print("2. IndexError        - indice fuera de rango")
        print("3. ZeroDivisionError - division entre cero")
        print("4. FileNotFoundError - archivo inexistente")
        print("5. IOError           - error de escritura")
        print("6. Volver al menu principal")

        opcion = None
        while opcion is None:
            try:
                opcion = input("Elige una opcion: ").strip()
                if opcion not in ["1", "2", "3", "4", "5", "6"]:
                    print("Opcion invalida, intenta de nuevo.")
                    opcion = None
            except ValueError:
                print("Opcion invalida, intenta de nuevo.")
                opcion = None

        if opcion == "1":
            try:
                int("abc")
            except ValueError:
                print("  [ValueError] Ocurrio porque se intento convertir el texto 'abc' a numero.")
                print("  Manejado con except ValueError: se ignoro el valor y el programa siguio.")

        elif opcion == "2":
            try:
                lista = [1, 2, 3]
                _ = lista[99]
            except IndexError:
                print("  [IndexError] Ocurrio porque se accedio al indice 99 en una lista de solo 3 elementos.")
                print("  Manejado con except IndexError: se evito el crash y el programa siguio.")

        elif opcion == "3":
            try:
                _ = 100 / 0
            except ZeroDivisionError:
                print("  [ZeroDivisionError] Ocurrio porque se intento dividir 100 entre 0, lo cual es matematicamente invalido.")
                print("  Manejado con except ZeroDivisionError: se capturo el error y el programa siguio.")

        elif opcion == "4":
            try:
                with open("archivo_inexistente.txt", "r") as archivo:
                    archivo.read()
            except FileNotFoundError:
                print("  [FileNotFoundError] Ocurrio porque se intento abrir 'archivo_inexistente.txt' y no existe.")
                print("  Manejado con except FileNotFoundError: se informo al usuario y el programa siguio.")

        elif opcion == "5":
            try:
                with open("/ruta/invalida/que/no/existe/archivo.txt", "w") as archivo:
                    archivo.write("datos")
            except IOError:
                print("  [IOError] Ocurrio porque se intento escribir en una ruta del sistema que no existe.")
                print("  Manejado con except IOError: se capturo el error de escritura y el programa siguio.")

        elif opcion == "6":
            break
