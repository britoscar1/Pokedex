from abc import ABC, abstractmethod


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
            try:
                self.nombre = self.evoluciones[self.evolucion - 1]
            except IndexError:
                self.evolucion -= 1
                return
            print(f"\n!El Pokemon ha evolucionado! Ahora es: {self.nombre}\n")
        elif self.nivel >= 100 and self.evolucion >= self.max_evolucion:
            self.nivel = 0
            print(f"\n{self.nombre} ya esta en su maxima evolucion. Nivel reiniciado a 0.\n")

    def entrenar(self):
        self.ataque += 10
        self.defensa += 10
        if self.evolucion < self.max_evolucion:
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
