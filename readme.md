# Mini Proyecto 2 - Batallas entre Pokémon

## Descripción
Este proyecto consiste en una aplicación de consola desarrollada en Python que permite gestionar Pokémon y simular batallas entre ellos.

El programa utiliza programación orientada a objetos mediante una clase `Pokemon` y una clase `SistemaPokemon`.

## Funcionalidades
- Cargar Pokémon desde un archivo CSV.
- Listar Pokémon registrados.
- Agregar nuevos Pokémon.
- Modificar Pokémon existentes.
- Eliminar Pokémon del sistema.
- Ver la tarjeta de características de cada Pokémon.
- Simular batallas entre dos Pokémon.

## Estructura del proyecto
mini_proyecto_2/
├── main.py
├── pokemon.csv
├── README.md
└── requirements.txt

## Archivo CSV
El archivo `pokemon.csv` contiene los siguientes datos:

- nombre
- tipo
- vida
- ataque
- defensa
- velocidad

## Reglas de batalla
La batalla se realiza entre dos Pokémon seleccionados por el usuario.

El Pokémon con mayor velocidad ataca primero.

El daño se calcula con la siguiente fórmula:

daño = ataque del atacante - mitad de la defensa del oponente

Si el daño es menor que 5, se asigna un daño mínimo de 5.

Gana el Pokémon que conserve vida al final de la batalla.

## Cómo ejecutar el proyecto
1. Descargar o clonar el repositorio.
2. Abrir la carpeta del proyecto.
3. Ejecutar el archivo principal con Python:

python main.py

## Tecnologías utilizadas
- Python
- CSV
- Programación orientada a objetos
- GitHub

## Autor
Kevin Alexander Carvajal Amezquita