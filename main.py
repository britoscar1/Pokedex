from base_datos import inicializar_bd, cargar_o_nueva_partida, guardar_partida
from combate import combatir
from archivos import ver_registro_batalla
from entrenamiento import menu_entrenamiento
from utilidades import crear_enemigos_iniciales, crear_enemigo_personalizado, pruebas_manejo_errores
from visual import banner_bienvenida, titulo_menu, color, VERDE, CYAN, AMARILLO


def main():
    try:
        banner_bienvenida()

        conexion = inicializar_bd()
        if conexion is None:
            print("No se pudo iniciar la base de datos. Saliendo.")
            return

        resultado = cargar_o_nueva_partida(conexion)
        if resultado is None:
            conexion.close()
            return

        nombre_jugador, mi_pokemon, lista_atrapados = resultado
        lista_enemigos = crear_enemigos_iniciales()

        while True:
            print()
            titulo_menu("MENU PRINCIPAL")
            print(color("  1.", CYAN), "Detalles de mi Pokemon")
            print(color("  2.", CYAN), "Hablar Pokemon")
            print(color("  3.", CYAN), "Entrenar Pokemon")
            print(color("  4.", CYAN), "Combatir")
            print(color("  5.", CYAN), "Ver Pokemon Atrapados")
            print(color("  6.", CYAN), "Crear Pokemon Enemigo")
            print(color("  7.", CYAN), "Pruebas de Manejo de Errores")
            print(color("  8.", CYAN), "Registros de Batallas")
            print(color("  9.", CYAN), "Guardar Partida")
            print(color(" 10.", CYAN), "Salir")

            opcion = None
            while opcion is None:
                try:
                    opcion = input("Elige una opcion: ").strip()
                    if opcion not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
                        print("Opcion invalida, intenta de nuevo.")
                        opcion = None
                except ValueError:
                    print("Error: debes ingresar una opcion valida.")
                    opcion = None

            if opcion == "1":
                mi_pokemon.detallesPokemon()
            elif opcion == "2":
                mi_pokemon.hablar()
            elif opcion == "3":
                menu_entrenamiento(mi_pokemon)
            elif opcion == "4":
                combatir(mi_pokemon, lista_enemigos, lista_atrapados, nombre_jugador)
            elif opcion == "5":
                mi_pokemon.verPokemonsAtrapados(lista_atrapados)
            elif opcion == "6":
                crear_enemigo_personalizado(lista_enemigos)
            elif opcion == "7":
                pruebas_manejo_errores()
            elif opcion == "8":
                ver_registro_batalla(nombre_jugador)
            elif opcion == "9":
                guardar_partida(conexion, nombre_jugador, mi_pokemon, lista_atrapados)
            elif opcion == "10":
                print(color(f"\nHasta luego, {nombre_jugador}! Fue un honor entrenar contigo.\n", AMARILLO))
                guardar_partida(conexion, nombre_jugador, mi_pokemon, lista_atrapados)
                conexion.close()
                break
    except Exception as e:
        print(f"\nError inesperado: {e}\n")


main()
