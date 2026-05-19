
from abc import ABC, abstractmethod
import random


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


def mostrar_stats_combate(p1, p2):
    print("\n----------------------------------------")
    print(f"  TU POKEMON  : {p1.nombre}")
    print(f"  Ataque: {p1.ataque}  Defensa: {p1.defensa}  Vida: {p1.vida}")
    print(f"  ENEMIGO     : {p2.nombre}")
    print(f"  Ataque: {p2.ataque}  Defensa: {p2.defensa}  Vida: {p2.vida}")
    print("----------------------------------------\n")


def combatir(mi_pokemon, lista_enemigos, lista_atrapados):
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
    while en_combate and mi_pokemon.vida > 0 and enemigo.vida > 0:
        print("--- TU TURNO ---")
        print("1. Pasar turno")
        print("2. Ataque normal")
        print("3. Ataque especial")
        print("4. Huir")

        opcion = input("Elige una opcion: ").strip()

        if opcion == "1":
            print(f"\n{mi_pokemon.nombre} paso su turno.")
        elif opcion == "2":
            danio = mi_pokemon.ataque
            print(f"\n{mi_pokemon.nombre} ataca! Dano: {danio}")
            aplicar_danio(danio, enemigo)
        elif opcion == "3":
            danio = int(mi_pokemon.ataque * 1.5)
            print(f"\n{mi_pokemon.nombre} usa {mi_pokemon.ataque_especial}! Dano: {danio}")
            aplicar_danio(danio, enemigo)
        elif opcion == "4":
            print(f"\n{mi_pokemon.nombre} huyo del combate!\n")
            enemigo.ataque = atk_orig
            enemigo.defensa = def_orig
            enemigo.vida = vida_orig
            return
        else:
            print("\nOpcion invalida, se paso el turno.")

        if enemigo.vida <= 0:
            print(f"\n{enemigo.nombre} fue derrotado!")
            if random.random() < 0.7:
                enemigo.atrapado = True
                lista_atrapados.append(enemigo)
                lista_enemigos.remove(enemigo)
                print(f"!Atrapaste a {enemigo.nombre}!\n")
            else:
                print(f"{enemigo.nombre} escapo antes de ser atrapado.\n")
                enemigo.ataque = atk_orig
                enemigo.defensa = def_orig
                enemigo.vida = vida_orig
            break

        print("\n--- TURNO DEL ENEMIGO ---")
        accion_enemigo = random.randint(1, 3)

        if accion_enemigo == 1:
            print(f"{enemigo.nombre} paso su turno.")
        elif accion_enemigo == 2:
            danio_enemigo = enemigo.ataque
            print(f"{enemigo.nombre} ataca! Dano: {danio_enemigo}")
            aplicar_danio(danio_enemigo, mi_pokemon)
        else:
            danio_enemigo = int(enemigo.ataque * 1.5)
            print(f"{enemigo.nombre} usa {enemigo.ataque_especial}! Dano: {danio_enemigo}")
            aplicar_danio(danio_enemigo, mi_pokemon)

        mostrar_stats_combate(mi_pokemon, enemigo)

        if mi_pokemon.vida <= 0:
            print(f"\n{mi_pokemon.nombre} fue derrotado. Fin del combate.\n")
            en_combate = False

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

        opcion = input("Elige una opcion: ").strip()

        if opcion == "1":
            mi_pokemon.entrenar()
            print("\n--- Stats actualizados ---")
            print(f"  Ataque: {mi_pokemon.ataque}  Defensa: {mi_pokemon.defensa}  Nivel: {mi_pokemon.nivel}\n")

        elif opcion == "2":
            print("\n1. Subir Ataque  (+20)")
            print("2. Subir Defensa (+20)")
            print("3. Subir Vida    (+20)")
            print("4. Cancelar")
            sub = input("Elige: ").strip()
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
            else:
                print("\nOpcion invalida.\n")

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
                print("\nValor invalido, regresando al menu de entrenamiento.\n")

        elif opcion == "5":
            break
        else:
            print("\nOpcion invalida.\n")


def crear_enemigo_personalizado(lista_enemigos):
    print("\n--- CREAR POKEMON ENEMIGO PERSONALIZADO ---")
    nombre = input("Nombre del Pokemon: ").strip()
    descripcion = input("Descripcion: ").strip()
    try:
        ataque = int(input("Ataque (1-1000): "))
        defensa = int(input("Defensa (1-1000): "))
        vida = int(input("Vida (1-1000): "))
    except ValueError:
        print("\nValor invalido, no se creo el enemigo.\n")
        return
    ataque_especial = input("Nombre del ataque especial: ").strip()

    print("\nElige el tipo:")
    print("1. Agua")
    print("2. Fuego")
    print("3. Electrico")
    print("4. Hierba")
    tipo = input("Tipo: ").strip()

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
    print("\n========================================")
    print("       BIENVENIDO A LA POKEDEX")
    print("========================================")

    nombre_jugador = input("Ingresa tu nombre de entrenador: ").strip()
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
        print("7. Salir")

        opcion = input("Elige una opcion: ").strip()

        if opcion == "1":
            mi_pokemon.detallesPokemon()
        elif opcion == "2":
            mi_pokemon.hablar()
        elif opcion == "3":
            menu_entrenamiento(mi_pokemon)
        elif opcion == "4":
            combatir(mi_pokemon, lista_enemigos, lista_atrapados)
        elif opcion == "5":
            mi_pokemon.verPokemonsAtrapados(lista_atrapados)
        elif opcion == "6":
            crear_enemigo_personalizado(lista_enemigos)
        elif opcion == "7":
            print(f"\nHasta luego, {nombre_jugador}! Fue un honor entrenar contigo.\n")
            break
        else:
            print("\nOpcion invalida, intenta de nuevo.\n")

main()

