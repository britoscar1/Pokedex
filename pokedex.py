
from abc import ABC, abstractmethod
import random
from datetime import datetime
import os


class PokemonBase(ABC):
    def __init__(self):
        self.nombre = "Sin Pokemon"
        self.descripcion = "No descripcion"
        self.ataque = 0
        self.defensa = 0
        self.vida = 0
        self.nivel = 0
        self.evolucion = 1
        self.atrapado = False

    @abstractmethod
    def hablar(self):
        pass

    @abstractmethod
    def actualizar(self):
        pass

    @abstractmethod
    def detallesPokemon(self):
        pass

    @abstractmethod
    def entrenar(self):
        pass


class Pokemon(PokemonBase):
    def __init__(self):
        super().__init__()
        self.boost_ataque = 20
        self.boost_defensa = 20
        self.boost_vida = 20
        self.evoluciones = []
        self.max_evolucion = 3

    def detallesPokemon(self):
        print("\n========================================")
        print(f"  Nombre      : {self.nombre}")
        print(f"  Descripcion : {self.descripcion}")
        print(f"  Ataque      : {self.ataque}")
        print(f"  Defensa     : {self.defensa}")
        print(f"  Vida        : {self.vida}")
        print(f"  Nivel       : {self.nivel}")
        print(f"  Evolucion   : {self.evolucion}")
        print(f"  Atrapado    : {self.atrapado}")
        print("========================================\n")

    def hablar(self):
        print(f"\n{self.nombre}!\n")

    def _verificarEvolucion(self):
        if self.nivel >= 100 and self.evolucion < self.max_evolucion:
            self.evolucion += 1
            self.nivel = 0
            self.nombre = self.evoluciones[self.evolucion - 1]
            print(f"\n!El Pokemon ha evolucionado! Ahora es: {self.nombre}\n")

    def entrenar(self):
        self.ataque += 10
        self.defensa += 10
        self.nivel += 10
        self._verificarEvolucion()

    def subirAtaque(self):
        self.ataque += self.boost_ataque

    def subirDefensa(self):
        self.defensa += self.boost_defensa

    def subirVida(self):
        self.vida += self.boost_vida

    def actualizar(self):
        self.ataque += self.boost_ataque
        self.defensa += self.boost_defensa
        self.vida += self.boost_vida

    def verPokemonsAtrapados(self, lista):
        if not lista:
            print("\nNo has atrapado ningun Pokemon aun.\n")
            return
        print("\n========================================")
        print("         POKEMON ATRAPADOS")
        print("========================================")
        for p in lista:
            p.detallesPokemon()


class Entrenamiento(ABC):
    @abstractmethod
    def subirAtaque(self):
        pass

    @abstractmethod
    def subirDefensa(self):
        pass

    @abstractmethod
    def subirVida(self):
        pass


class PokemonConEntrenamiento(Pokemon, Entrenamiento):
    pass


class PokemonAgua(PokemonConEntrenamiento):
    def __init__(self):
        super().__init__()
        self.ataque_especial = "Hidrobomba"
        self.evoluciones = ["Squirtle", "Wartortle", "Blastoise"]
        self.max_evolucion = 3
        self.nombre = self.evoluciones[0]
        self.descripcion = "Pokemon tipo Agua"
        self.ataque = 44
        self.defensa = 65
        self.vida = 100

    def actualizar(self):
        self.ataque += 15
        self.defensa += 25
        self.vida += 20

    def hablar(self):
        sonidos = ["Squirtle!", "Wartortle!", "Blastoise!"]
        print(f"\n{sonidos[self.evolucion - 1]}\n")


class PokemonFuego(PokemonConEntrenamiento):
    def __init__(self):
        super().__init__()
        self.ataque_especial = "Lanzallamas"
        self.evoluciones = ["Charmander", "Charmeleon", "Charizard"]
        self.max_evolucion = 3
        self.nombre = self.evoluciones[0]
        self.descripcion = "Pokemon tipo Fuego"
        self.ataque = 52
        self.defensa = 43
        self.vida = 100

    def actualizar(self):
        self.ataque += 25
        self.defensa += 15
        self.vida += 20

    def hablar(self):
        sonidos = ["Charmander!", "Charmeleon!", "Charizard!"]
        print(f"\n{sonidos[self.evolucion - 1]}\n")


class PokemonElectrico(PokemonConEntrenamiento):
    def __init__(self):
        super().__init__()
        self.ataque_especial = "Impactrueno"
        self.evoluciones = ["Pichu", "Pikachu", "Raichu"]
        self.max_evolucion = 3
        self.nombre = self.evoluciones[0]
        self.descripcion = "Pokemon tipo Electrico"
        self.ataque = 55
        self.defensa = 40
        self.vida = 90

    def actualizar(self):
        self.ataque += 20
        self.defensa += 10
        self.vida += 30

    def hablar(self):
        sonidos = ["Pichu!", "Pikachu!", "Raichu!"]
        print(f"\n{sonidos[self.evolucion - 1]}\n")


class PokemonHierba(PokemonConEntrenamiento):
    def __init__(self):
        super().__init__()
        self.ataque_especial = "Latigo Cepa"
        self.evoluciones = ["Bulbasaur", "Ivysaur", "Venusaur"]
        self.max_evolucion = 3
        self.nombre = self.evoluciones[0]
        self.descripcion = "Pokemon tipo Hierba"
        self.ataque = 49
        self.defensa = 49
        self.vida = 100

    def actualizar(self):
        self.ataque += 15
        self.defensa += 20
        self.vida += 25

    def hablar(self):
        sonidos = ["Bulbasaur!", "Ivysaur!", "Venusaur!"]
        print(f"\n{sonidos[self.evolucion - 1]}\n")


def aplicar_danio(danio, defensor):
    if danio >= defensor.defensa:
        sobrante = danio - defensor.defensa
        defensor.defensa = 0
        defensor.vida = max(0, defensor.vida - sobrante)
    else:
        defensor.defensa -= danio


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


def pruebas_manejo_errores():
    print("\n========================================")
    print("    PRUEBAS DE MANEJO DE ERRORES")
    print("========================================\n")

    print("--- Prueba 1: ValueError (entrada numerica invalida) ---")
    try:
        numero = int(input("Intenta escribir 'abc' en lugar de un numero: "))
        print(f"Numero ingresado: {numero}")
    except ValueError:
        print("Error capturado: ValueError - No es un numero valido.")
    print()

    print("--- Prueba 2: IndexError (acceso a indice invalido) ---")
    try:
        lista = [1, 2, 3]
        print(f"Lista: {lista}")
        print(f"Accediendo a indice 99: {lista[99]}")
    except IndexError:
        print("Error capturado: IndexError - Indice fuera de rango.")
    print()

    print("--- Prueba 3: ZeroDivisionError (division entre cero) ---")
    try:
        resultado = 100 / 0
    except ZeroDivisionError:
        print("Error capturado: ZeroDivisionError - No se puede dividir entre cero.")
    print()

    print("--- Prueba 4: FileNotFoundError (archivo no existe) ---")
    try:
        with open("archivo_inexistente.txt", "r") as archivo:
            contenido = archivo.read()
    except FileNotFoundError:
        print("Error capturado: FileNotFoundError - El archivo no existe.")
    print()

    print("--- Prueba 5: IOError (error de lectura) ---")
    try:
        with open("/dev/null", "r") as archivo:
            linea = archivo.readline()
            print("Lectura exitosa.")
    except IOError as e:
        print(f"Error capturado: IOError - {e}")
    print()

    print("Todas las pruebas completadas sin detener el programa.\n")


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


def menu_entrenamiento(mi_pokemon):
    while True:
        print("\n========================================")
        print("         ENTRENAR POKEMON")
        print("========================================")
        print("1. Entrenamiento Normal      (ataque, defensa, nivel +10)")
        print("2. Entrenamiento Individual  (sube un atributo +20)")
        print("3. Entrenamiento Intensivo   (ataque, defensa, vida +20)")
        print("4. Entrenamiento Personalizado (valores manuales)")
        print("5. Volver al menu principal")

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
            try:
                nuevo_ataque = int(input("Nuevo ataque (1-1000): "))
                nuevo_defensa = int(input("Nueva defensa (1-1000): "))
                nuevo_vida = int(input("Nueva vida (1-1000): "))
                nuevo_nivel = int(input("Nuevo nivel (0-100): "))
                mi_pokemon.ataque = nuevo_ataque
                mi_pokemon.defensa = nuevo_defensa
                mi_pokemon.vida = nuevo_vida
                mi_pokemon.nivel = nuevo_nivel
                print("\n--- Stats actualizados ---")
                print(f"  Ataque: {mi_pokemon.ataque}  Defensa: {mi_pokemon.defensa}")
                print(f"  Vida: {mi_pokemon.vida}  Nivel: {mi_pokemon.nivel}\n")
                mi_pokemon._verificarEvolucion()
            except ValueError:
                print("\nError: todos los valores deben ser numeros. Regresando al menu.\n")

        elif opcion == "5":
            break


def crear_enemigo_personalizado(lista_enemigos):
    print("\n--- CREAR POKEMON ENEMIGO PERSONALIZADO ---")
    nombre = input("Nombre del Pokemon: ").strip()
    descripcion = input("Descripcion: ").strip()

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
    enemigo4.descripcion = "Pokemon Electrico pequeño y debil"
    enemigo4.ataque = 20
    enemigo4.defensa = 15
    enemigo4.vida = 35
    enemigo4.ataque_especial = "Impactrueno"

    return [enemigo1, enemigo2, enemigo3, enemigo4]


def main():
    try:
        print("\n========================================")
        print("       BIENVENIDO A LA POKEDEX")
        print("========================================")

        nombre_jugador = None
        while nombre_jugador is None:
            try:
                nombre_jugador = input("Ingresa tu nombre de entrenador: ").strip()
                if not nombre_jugador:
                    print("Error: el nombre no puede estar vacio.")
                    nombre_jugador = None
            except ValueError:
                print("Error: ingresa un nombre valido.")
                nombre_jugador = None

        print(f"\nHola, {nombre_jugador}!")
        print("Aun no tienes un Pokemon. Debes elegir uno para comenzar.\n")

        mi_pokemon = elegir_pokemon()
        print(f"\nElegiste a {mi_pokemon.nombre}! Aqui estan sus detalles:")
        mi_pokemon.detallesPokemon()

        lista_enemigos = crear_enemigos_iniciales()
        lista_atrapados = []

        while True:
            print("\n========================================")
            print("          MENU PRINCIPAL")
            print("========================================")
            print("1. Detalles de mi Pokemon")
            print("2. Hablar Pokemon")
            print("3. Entrenar Pokemon")
            print("4. Combatir")
            print("5. Ver Pokemon Atrapados")
            print("6. Crear Pokemon Enemigo")
            print("7. Pruebas de Manejo de Errores")
            print("8. Registros de Batallas")
            print("9. Guardar Partida")
            print("10. Salir")

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
                ver_registro_batalla()
            elif opcion == "9":
                print("\n(Esta opcion sera completada en la siguiente parte)\n")
            elif opcion == "10":
                print(f"\nHasta luego, {nombre_jugador}! Fue un honor entrenar contigo.\n")
                break
    except Exception as e:
        print(f"\nError inesperado: {e}\n")

main()

