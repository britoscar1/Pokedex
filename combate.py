import random

from archivos import guardar_registro_batalla


def aplicar_danio(danio, defensor):
    if danio >= defensor.defensa:
        sobrante = danio - defensor.defensa
        defensor.defensa = 0
        defensor.vida = max(0, defensor.vida - sobrante)
    else:
        defensor.defensa -= danio


def mostrar_stats_combate(p1, p2):
    print("\n----------------------------------------")
    print(f"  TU POKEMON  : {p1.nombre}")
    print(f"  Ataque: {p1.ataque}  Defensa: {p1.defensa}  Vida: {p1.vida}")
    print(f"  ENEMIGO     : {p2.nombre}")
    print(f"  Ataque: {p2.ataque}  Defensa: {p2.defensa}  Vida: {p2.vida}")
    print("----------------------------------------\n")


def combatir(mi_pokemon, lista_enemigos, lista_atrapados, nombre_entrenador):
    if not lista_enemigos:
        print("\nNo hay enemigos disponibles para combatir.\n")
        return

    enemigo = random.choice(lista_enemigos)

    atk_orig = enemigo.ataque
    def_orig = enemigo.defensa
    vida_orig = enemigo.vida

    print(f"\n!Un {enemigo.nombre} salvaje aparecio!")
    mostrar_stats_combate(mi_pokemon, enemigo)

    en_combate = True
    log_lineas = []
    numero_turno = 1

    while en_combate and mi_pokemon.vida > 0 and enemigo.vida > 0:
        log_lineas.append(f"== TURNO {numero_turno} ==")

        print("--- TU TURNO ---")
        print("1. Pasar turno")
        print("2. Ataque normal")
        print("3. Ataque especial")
        print("4. Huir")

        opcion = None
        while opcion is None:
            try:
                opcion = input("Elige una opcion: ").strip()
                if opcion not in ["1", "2", "3", "4"]:
                    print("Opcion invalida, intenta de nuevo.")
                    opcion = None
            except ValueError:
                print("Error: debes ingresar una opcion valida.")
                opcion = None

        if opcion == "1":
            print(f"\n{mi_pokemon.nombre} paso su turno.")
            log_lineas.append(f"{mi_pokemon.nombre} paso su turno.")
        elif opcion == "2":
            danio = mi_pokemon.ataque
            print(f"\n{mi_pokemon.nombre} ataca! Dano: {danio}")
            log_lineas.append(f"{mi_pokemon.nombre} usa ataque normal")
            log_lineas.append(f"Dano de ataque: {danio}")
            aplicar_danio(danio, enemigo)
            log_lineas.append(f"Stats del Pokemon Enemigo - Defensa: {enemigo.defensa} Vida: {enemigo.vida}")
        elif opcion == "3":
            danio = int(mi_pokemon.ataque * 1.5)
            print(f"\n{mi_pokemon.nombre} usa {mi_pokemon.ataque_especial}! Dano: {danio}")
            log_lineas.append(f"{mi_pokemon.nombre} usa ataque especial")
            log_lineas.append(f"Dano de ataque: {danio}")
            aplicar_danio(danio, enemigo)
            log_lineas.append(f"Stats del Pokemon Enemigo - Defensa: {enemigo.defensa} Vida: {enemigo.vida}")
        elif opcion == "4":
            print(f"\n{mi_pokemon.nombre} huyo del combate!\n")
            enemigo.ataque = atk_orig
            enemigo.defensa = def_orig
            enemigo.vida = vida_orig
            return

        if enemigo.vida <= 0:
            print(f"\n{enemigo.nombre} fue derrotado!")
            if random.random() < 0.7:
                enemigo.atrapado = True
                lista_atrapados.append(enemigo)
                lista_enemigos.remove(enemigo)
                print(f"!Atrapaste a {enemigo.nombre}!\n")
                resultado = "Victoria! Has derrotado al Pokemon enemigo y lo has atrapado!"
                log_lineas.append(f"Resultado: {resultado}")
                guardar_registro_batalla(nombre_entrenador, mi_pokemon, enemigo, resultado, log_lineas)
            else:
                print(f"{enemigo.nombre} escapo antes de ser atrapado.\n")
                enemigo.ataque = atk_orig
                enemigo.defensa = def_orig
                enemigo.vida = vida_orig
                resultado = "Victoria pero el Pokemon escapo"
                log_lineas.append(f"Resultado: {resultado}")
                guardar_registro_batalla(nombre_entrenador, mi_pokemon, enemigo, resultado, log_lineas)
            break

        print("\n--- TURNO DEL ENEMIGO ---")
        accion_enemigo = random.randint(1, 3)

        if accion_enemigo == 1:
            print(f"{enemigo.nombre} paso su turno.")
            log_lineas.append(f"{enemigo.nombre} paso su turno.")
        elif accion_enemigo == 2:
            danio_enemigo = enemigo.ataque
            print(f"{enemigo.nombre} ataca! Dano: {danio_enemigo}")
            log_lineas.append(f"{enemigo.nombre} usa ataque normal")
            log_lineas.append(f"Dano de ataque: {danio_enemigo}")
            aplicar_danio(danio_enemigo, mi_pokemon)
            log_lineas.append(f"Stats de mi Pokemon - Defensa: {mi_pokemon.defensa} Vida: {mi_pokemon.vida}")
        else:
            danio_enemigo = int(enemigo.ataque * 1.5)
            print(f"{enemigo.nombre} usa {enemigo.ataque_especial}! Dano: {danio_enemigo}")
            log_lineas.append(f"{enemigo.nombre} usa ataque especial")
            log_lineas.append(f"Dano de ataque: {danio_enemigo}")
            aplicar_danio(danio_enemigo, mi_pokemon)
            log_lineas.append(f"Stats de mi Pokemon - Defensa: {mi_pokemon.defensa} Vida: {mi_pokemon.vida}")

        mostrar_stats_combate(mi_pokemon, enemigo)

        if mi_pokemon.vida <= 0:
            print(f"\n{mi_pokemon.nombre} fue derrotado. Fin del combate.\n")
            en_combate = False
            resultado = "Derrota"
            log_lineas.append(f"Resultado: {resultado}")
            guardar_registro_batalla(nombre_entrenador, mi_pokemon, enemigo, resultado, log_lineas)

        numero_turno += 1

    if en_combate and enemigo.vida > 0:
        enemigo.ataque = atk_orig
        enemigo.defensa = def_orig
        enemigo.vida = vida_orig
