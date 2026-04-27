import csv
import random


class Pokemon:
    def __init__(self, nombre, tipo, vida, ataque, defensa, velocidad):
        self.nombre = nombre
        self.tipo = tipo
        self.vida = int(vida)
        self.ataque = int(ataque)
        self.defensa = int(defensa)
        self.velocidad = int(velocidad)

    def mostrar_tarjeta(self):
        print("\n--- Tarjeta Pokémon ---")
        print(f"Nombre: {self.nombre}")
        print(f"Tipo: {self.tipo}")
        print(f"Vida: {self.vida}")
        print(f"Ataque: {self.ataque}")
        print(f"Defensa: {self.defensa}")
        print(f"Velocidad: {self.velocidad}")

    def calcular_dano(self, oponente):
        dano = self.ataque - (oponente.defensa // 2)
        if dano < 5:
            dano = 5
        return dano


class SistemaPokemon:
    def __init__(self):
        self.pokemones = []

    def cargar_desde_csv(self, archivo):
        try:
            with open(archivo, mode="r", encoding="utf-8") as file:
                lector = csv.DictReader(file)

                for fila in lector:
                    pokemon = Pokemon(
                        fila["nombre"],
                        fila["tipo"],
                        fila["vida"],
                        fila["ataque"],
                        fila["defensa"],
                        fila["velocidad"]
                    )
                    self.pokemones.append(pokemon)

            print("Pokémon cargados correctamente.")

        except FileNotFoundError:
            print("No se encontró el archivo pokemon.csv.")

    def guardar_en_csv(self, archivo):
        with open(archivo, mode="w", encoding="utf-8", newline="") as file:
            campos = ["nombre", "tipo", "vida", "ataque", "defensa", "velocidad"]
            escritor = csv.DictWriter(file, fieldnames=campos)

            escritor.writeheader()

            for pokemon in self.pokemones:
                escritor.writerow({
                    "nombre": pokemon.nombre,
                    "tipo": pokemon.tipo,
                    "vida": pokemon.vida,
                    "ataque": pokemon.ataque,
                    "defensa": pokemon.defensa,
                    "velocidad": pokemon.velocidad
                })

    def listar_pokemones(self):
        if not self.pokemones:
            print("No hay Pokémon registrados.")
            return

        print("\n--- Lista de Pokémon ---")
        for i, pokemon in enumerate(self.pokemones, start=1):
            print(f"{i}. {pokemon.nombre} - Tipo: {pokemon.tipo}")

    def agregar_pokemon(self):
        print("\n--- Agregar Pokémon ---")
        nombre = input("Nombre: ")
        tipo = input("Tipo: ")
        vida = int(input("Vida: "))
        ataque = int(input("Ataque: "))
        defensa = int(input("Defensa: "))
        velocidad = int(input("Velocidad: "))

        nuevo_pokemon = Pokemon(nombre, tipo, vida, ataque, defensa, velocidad)
        self.pokemones.append(nuevo_pokemon)
        self.guardar_en_csv("pokemon.csv")

        print("Pokémon agregado correctamente.")

    def modificar_pokemon(self):
        self.listar_pokemones()

        nombre = input("\nDigite el nombre del Pokémon que desea modificar: ")

        for pokemon in self.pokemones:
            if pokemon.nombre.lower() == nombre.lower():
                print("Deje vacío un campo si no desea modificarlo.")

                nuevo_tipo = input(f"Nuevo tipo ({pokemon.tipo}): ")
                nueva_vida = input(f"Nueva vida ({pokemon.vida}): ")
                nuevo_ataque = input(f"Nuevo ataque ({pokemon.ataque}): ")
                nueva_defensa = input(f"Nueva defensa ({pokemon.defensa}): ")
                nueva_velocidad = input(f"Nueva velocidad ({pokemon.velocidad}): ")

                if nuevo_tipo:
                    pokemon.tipo = nuevo_tipo
                if nueva_vida:
                    pokemon.vida = int(nueva_vida)
                if nuevo_ataque:
                    pokemon.ataque = int(nuevo_ataque)
                if nueva_defensa:
                    pokemon.defensa = int(nueva_defensa)
                if nueva_velocidad:
                    pokemon.velocidad = int(nueva_velocidad)

                self.guardar_en_csv("pokemon.csv")
                print("Pokémon modificado correctamente.")
                return

        print("Pokémon no encontrado.")

    def eliminar_pokemon(self):
        self.listar_pokemones()

        nombre = input("\nDigite el nombre del Pokémon que desea eliminar: ")

        for pokemon in self.pokemones:
            if pokemon.nombre.lower() == nombre.lower():
                self.pokemones.remove(pokemon)
                self.guardar_en_csv("pokemon.csv")
                print("Pokémon eliminado correctamente.")
                return

        print("Pokémon no encontrado.")

    def buscar_pokemon(self, nombre):
        for pokemon in self.pokemones:
            if pokemon.nombre.lower() == nombre.lower():
                return pokemon
        return None

    def batalla(self):
        print("\n--- Batalla Pokémon ---")
        self.listar_pokemones()

        nombre1 = input("\nDigite el nombre del primer Pokémon: ")
        nombre2 = input("Digite el nombre del segundo Pokémon: ")

        pokemon1 = self.buscar_pokemon(nombre1)
        pokemon2 = self.buscar_pokemon(nombre2)

        if pokemon1 is None or pokemon2 is None:
            print("Uno o ambos Pokémon no fueron encontrados.")
            return

        vida1 = pokemon1.vida
        vida2 = pokemon2.vida

        print(f"\nComienza la batalla entre {pokemon1.nombre} y {pokemon2.nombre}.")

        if pokemon1.velocidad >= pokemon2.velocidad:
            atacante = pokemon1
            defensor = pokemon2
        else:
            atacante = pokemon2
            defensor = pokemon1

        while vida1 > 0 and vida2 > 0:
            dano = atacante.calcular_dano(defensor)

            if defensor == pokemon1:
                vida1 -= dano
                print(f"{atacante.nombre} ataca a {defensor.nombre} y causa {dano} de daño. Vida restante de {defensor.nombre}: {max(vida1, 0)}")
            else:
                vida2 -= dano
                print(f"{atacante.nombre} ataca a {defensor.nombre} y causa {dano} de daño. Vida restante de {defensor.nombre}: {max(vida2, 0)}")

            atacante, defensor = defensor, atacante

        if vida1 > 0:
            print(f"\nGanador: {pokemon1.nombre}")
        else:
            print(f"\nGanador: {pokemon2.nombre}")


def menu():
    sistema = SistemaPokemon()
    sistema.cargar_desde_csv("pokemon.csv")

    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Listar Pokémon")
        print("2. Agregar Pokémon")
        print("3. Modificar Pokémon")
        print("4. Eliminar Pokémon")
        print("5. Batalla Pokémon")
        print("6. Ver tarjeta de un Pokémon")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            sistema.listar_pokemones()
        elif opcion == "2":
            sistema.agregar_pokemon()
        elif opcion == "3":
            sistema.modificar_pokemon()
        elif opcion == "4":
            sistema.eliminar_pokemon()
        elif opcion == "5":
            sistema.batalla()
        elif opcion == "6":
            nombre = input("Digite el nombre del Pokémon: ")
            pokemon = sistema.buscar_pokemon(nombre)

            if pokemon:
                pokemon.mostrar_tarjeta()
            else:
                print("Pokémon no encontrado.")
        elif opcion == "7":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


menu()