from visual import titulo_menu, color, CYAN


def menu_entrenamiento(mi_pokemon):
    while True:
        print()
        titulo_menu("ENTRENAR POKEMON")
        print(color("  1.", CYAN), "Entrenamiento Normal      (ataque, defensa, nivel +10)")
        print(color("  2.", CYAN), "Entrenamiento Individual  (sube un atributo +20)")
        print(color("  3.", CYAN), "Entrenamiento Intensivo   (ataque, defensa, vida +20)")
        print(color("  4.", CYAN), "Entrenamiento Personalizado (valores manuales)")
        print(color("  5.", CYAN), "Volver al menu principal")

        opcion = None
        while opcion is None:
            try:
                opcion = input("Elige una opcion: ").strip()
                if opcion not in ["1", "2", "3", "4", "5"]:
                    print("Opcion invalida, intenta de nuevo.")
                    opcion = None
            except ValueError:
                print("Error: debes ingresar una opcion valida.")
                opcion = None

        if opcion == "1":
            mi_pokemon.entrenar()
            print("\n--- Stats actualizados ---")
            print(f"  Ataque: {mi_pokemon.ataque}  Defensa: {mi_pokemon.defensa}  Nivel: {mi_pokemon.nivel}\n")

        elif opcion == "2":
            print("\n1. Subir Ataque  (+20)")
            print("2. Subir Defensa (+20)")
            print("3. Subir Vida    (+20)")
            print("4. Cancelar")
            sub = None
            while sub is None:
                try:
                    sub = input("Elige: ").strip()
                    if sub not in ["1", "2", "3", "4"]:
                        print("Opcion invalida, intenta de nuevo.")
                        sub = None
                except ValueError:
                    print("Error: debes ingresar una opcion valida.")
                    sub = None

            if sub == "1":
                mi_pokemon.subirAtaque()
                print(f"\nAtaque aumentado. Ataque actual: {mi_pokemon.ataque}\n")
            elif sub == "2":
                mi_pokemon.subirDefensa()
                print(f"\nDefensa aumentada. Defensa actual: {mi_pokemon.defensa}\n")
            elif sub == "3":
                mi_pokemon.subirVida()
                print(f"\nVida aumentada. Vida actual: {mi_pokemon.vida}\n")
            elif sub == "4":
                pass

        elif opcion == "3":
            mi_pokemon.actualizar()
            print("\n--- Stats actualizados ---")
            print(f"  Ataque: {mi_pokemon.ataque}  Defensa: {mi_pokemon.defensa}  Vida: {mi_pokemon.vida}\n")

        elif opcion == "4":
            print("\nIngresa los nuevos valores:")

            nuevo_ataque = None
            while nuevo_ataque is None:
                try:
                    nuevo_ataque = int(input("Nuevo ataque (1-1000): "))
                    if nuevo_ataque < 1 or nuevo_ataque > 1000:
                        print("Valor fuera de rango, ingresa entre 1 y 1000.")
                        nuevo_ataque = None
                except ValueError:
                    print("Error: debes ingresar un numero valido.")

            nuevo_defensa = None
            while nuevo_defensa is None:
                try:
                    nuevo_defensa = int(input("Nueva defensa (1-1000): "))
                    if nuevo_defensa < 1 or nuevo_defensa > 1000:
                        print("Valor fuera de rango, ingresa entre 1 y 1000.")
                        nuevo_defensa = None
                except ValueError:
                    print("Error: debes ingresar un numero valido.")

            nuevo_vida = None
            while nuevo_vida is None:
                try:
                    nuevo_vida = int(input("Nueva vida (1-1000): "))
                    if nuevo_vida < 1 or nuevo_vida > 1000:
                        print("Valor fuera de rango, ingresa entre 1 y 1000.")
                        nuevo_vida = None
                except ValueError:
                    print("Error: debes ingresar un numero valido.")

            nuevo_nivel = None
            while nuevo_nivel is None:
                try:
                    nuevo_nivel = int(input("Nuevo nivel (0-100): "))
                    if nuevo_nivel < 0 or nuevo_nivel > 100:
                        print("Valor fuera de rango, ingresa entre 0 y 100.")
                        nuevo_nivel = None
                except ValueError:
                    print("Error: debes ingresar un numero valido.")

            mi_pokemon.ataque = nuevo_ataque
            mi_pokemon.defensa = nuevo_defensa
            mi_pokemon.vida = nuevo_vida
            mi_pokemon.nivel = nuevo_nivel
            print("\n--- Stats actualizados ---")
            print(f"  Ataque: {mi_pokemon.ataque}  Defensa: {mi_pokemon.defensa}")
            print(f"  Vida: {mi_pokemon.vida}  Nivel: {mi_pokemon.nivel}\n")
            mi_pokemon._verificarEvolucion()

        elif opcion == "5":
            break
