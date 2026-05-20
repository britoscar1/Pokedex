import sqlite3
from datetime import datetime

from modelos import PokemonAgua, PokemonFuego, PokemonElectrico, PokemonHierba
from utilidades import elegir_pokemon, _obtener_tipo_string


def inicializar_bd():
    try:
        conexion = sqlite3.connect("pokedex.db")
        cursor = conexion.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS partidas (
                id INTEGER PRIMARY KEY,
                nombre_entrenador TEXT,
                fecha_guardado TEXT,
                pokemon_nombre TEXT,
                pokemon_tipo TEXT,
                pokemon_ataque INTEGER,
                pokemon_defensa INTEGER,
                pokemon_vida INTEGER,
                pokemon_nivel INTEGER,
                pokemon_evolucion INTEGER
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS capturados (
                id INTEGER PRIMARY KEY,
                partida_id INTEGER,
                nombre TEXT,
                tipo TEXT,
                ataque INTEGER,
                defensa INTEGER,
                vida INTEGER,
                nivel INTEGER,
                FOREIGN KEY (partida_id) REFERENCES partidas(id)
            )
        """)
        conexion.commit()
        return conexion
    except sqlite3.Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None


def reconstruir_pokemon(tipo, nombre, ataque, defensa, vida, nivel, evolucion):
    try:
        if tipo == "Agua":
            p = PokemonAgua()
        elif tipo == "Fuego":
            p = PokemonFuego()
        elif tipo == "Electrico":
            p = PokemonElectrico()
        elif tipo == "Hierba":
            p = PokemonHierba()
        else:
            raise ValueError(f"Tipo de Pokemon desconocido: {tipo}")
        p.nombre = nombre
        p.ataque = ataque
        p.defensa = defensa
        p.vida = vida
        p.nivel = nivel
        p.evolucion = evolucion
        return p
    except ValueError as e:
        print(f"Error al reconstruir Pokemon: {e}")
        return None


def cargar_o_nueva_partida(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM partidas ORDER BY fecha_guardado DESC")
        partidas = cursor.fetchall()

        if not partidas:
            resp = None
            while resp is None:
                try:
                    resp = input("No hay partidas guardadas. Deseas iniciar una nueva partida? (s/n): ").strip().lower()
                    if resp not in ["s", "n"]:
                        print("Opcion invalida, ingresa 's' o 'n'.")
                        resp = None
                except ValueError:
                    print("Opcion invalida, ingresa 's' o 'n'.")
                    resp = None
            if resp == "s":
                nombre_entrenador = None
                while nombre_entrenador is None:
                    try:
                        nombre_entrenador = input("Ingresa tu nombre de entrenador: ").strip()
                        if not nombre_entrenador:
                            print("Error: el nombre no puede estar vacio.")
                            nombre_entrenador = None
                    except ValueError:
                        print("Error: ingresa un nombre valido.")
                        nombre_entrenador = None
                mi_pokemon = elegir_pokemon()
                return (nombre_entrenador, mi_pokemon, [])
            else:
                print("Hasta luego!")
                return None
        else:
            print("\n========================================")
            print("         PARTIDAS GUARDADAS")
            print("========================================")
            for i, p in enumerate(partidas):
                print(f"{i + 1}. [{p[2]}] {p[1]} – {p[3]}")

            seleccion = None
            while seleccion is None:
                try:
                    seleccion = int(input("Selecciona una partida (numero): ")) - 1
                    if seleccion < 0 or seleccion >= len(partidas):
                        print("Seleccion invalida, intenta de nuevo.")
                        seleccion = None
                except ValueError:
                    print("Error: debes ingresar un numero valido.")
                    seleccion = None

            partida = partidas[seleccion]
            partida_id = partida[0]
            nombre_entrenador = partida[1]

            mi_pokemon = reconstruir_pokemon(
                partida[4], partida[3], partida[5], partida[6],
                partida[7], partida[8], partida[9]
            )
            if mi_pokemon is None:
                print("Error: no se pudo reconstruir el Pokemon de la partida. Iniciando con Pokemon por defecto.")
                mi_pokemon = elegir_pokemon()

            cursor.execute("SELECT * FROM capturados WHERE partida_id = ?", (partida_id,))
            capturados_rows = cursor.fetchall()

            lista_atrapados = []
            for row in capturados_rows:
                p = reconstruir_pokemon(row[3], row[2], row[4], row[5], row[6], row[7], 1)
                if p:
                    p.atrapado = True
                    lista_atrapados.append(p)

            print(f"\nBienvenido de nuevo {nombre_entrenador}!")
            mi_pokemon.detallesPokemon()

            return (nombre_entrenador, mi_pokemon, lista_atrapados)
    except sqlite3.Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None


def guardar_partida(conexion, nombre_entrenador, mi_pokemon, lista_atrapados):
    resp = None
    while resp is None:
        try:
            resp = input("Deseas guardar el progreso actual? (s/n): ").strip().lower()
            if resp not in ["s", "n"]:
                print("Opcion invalida, ingresa 's' o 'n'.")
                resp = None
        except ValueError:
            print("Opcion invalida, ingresa 's' o 'n'.")
            resp = None
    if resp != "s":
        return
    try:
        tipo = _obtener_tipo_string(mi_pokemon)
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM partidas WHERE nombre_entrenador = ?", (nombre_entrenador,))
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("""
            INSERT INTO partidas (nombre_entrenador, fecha_guardado, pokemon_nombre, pokemon_tipo,
                                  pokemon_ataque, pokemon_defensa, pokemon_vida, pokemon_nivel, pokemon_evolucion)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (nombre_entrenador, fecha, mi_pokemon.nombre, tipo,
              mi_pokemon.ataque, mi_pokemon.defensa, mi_pokemon.vida,
              mi_pokemon.nivel, mi_pokemon.evolucion))
        partida_id = cursor.lastrowid
        for p in lista_atrapados:
            tipo_p = _obtener_tipo_string(p)
            cursor.execute("""
                INSERT INTO capturados (partida_id, nombre, tipo, ataque, defensa, vida, nivel)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (partida_id, p.nombre, tipo_p, p.ataque, p.defensa, p.vida, p.nivel))
        conexion.commit()
        print("Partida guardada correctamente.")
    except sqlite3.Error as e:
        print(f"Error al guardar la partida: {e}")
