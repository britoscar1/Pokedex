from datetime import datetime
import os


def generar_nombre_batalla():
    ahora = datetime.now()
    fecha_str = ahora.strftime("%d-%m-%y")
    hora_str = ahora.strftime("%H-%M")
    return f"batalla_{fecha_str}_{hora_str}.txt"


def guardar_registro_batalla(nombre_entrenador, mi_pokemon, enemigo, resultado, log_lineas):
    try:
        nombre_archivo = generar_nombre_batalla()

        with open(nombre_archivo, "w") as archivo:
            archivo.write("=== COMBATE ===\n")
            archivo.write(f"Entrenador: {nombre_entrenador}\n")
            archivo.write(f"Pokemon: {mi_pokemon.nombre}\n")
            archivo.write(f"Detalles: ataque={mi_pokemon.ataque} defensa={mi_pokemon.defensa} vida={mi_pokemon.vida}\n")
            archivo.write(f"Enemigo: {enemigo.nombre}\n")
            archivo.write(f"Detalles Enemigo: ataque={enemigo.ataque} defensa={enemigo.defensa} vida={enemigo.vida}\n")

            for linea in log_lineas:
                archivo.write(linea + "\n")

            archivo.write(f"Resultado: {resultado}\n")

            ahora = datetime.now()
            fecha_hora = ahora.strftime("%d-%m-%Y %H:%M")
            archivo.write(f"Fecha y hora de la batalla: {fecha_hora}\n")
            archivo.write("-" * 26 + "\n")

        return nombre_archivo
    except IOError as e:
        print(f"\nError al guardar el archivo de batalla: {e}\n")
        return None


def ver_registro_batalla():
    try:
        archivos_batalla = [f for f in os.listdir(".") if f.startswith("batalla_") and f.endswith(".txt")]

        if not archivos_batalla:
            print("\nNo hay registros de batallas disponibles.\n")
            return

        archivos_batalla.sort(reverse=True)

        print("\n========================================")
        print("       REGISTROS DE BATALLAS")
        print("========================================\n")

        try:
            with open(archivos_batalla[0], "r") as archivo:
                contenido = archivo.read()
                print(contenido)
        except FileNotFoundError:
            print(f"\nEl archivo {archivos_batalla[0]} no fue encontrado.\n")
        except IOError as e:
            print(f"\nError al leer el archivo: {e}\n")
    except Exception as e:
        print(f"\nError al acceder a los registros: {e}\n")
