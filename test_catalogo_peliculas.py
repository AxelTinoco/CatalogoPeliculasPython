from Domain.Pelicula import Pelicula
from Service.catalogo_peliculas import CatalogoPeliculas as cp
option = None

while option != 4:
    try:
        print('Opciones:')
        print('1. Agregar Pelicula')
        print('2. Listar Peliculas')
        print('3. Eliminar Catalogo Peliculas')
        print('4. Sale')
        option = int(input('Escibe tu opcion (1-4)'))

        if option == 1:
            nombre_pelicula = input('Nombre de Pelicula:')
            pelicula = Pelicula(nombre_pelicula)
            cp.agregar_pelicula(pelicula)
        elif option == 2:
            cp.listar_peliula()
        elif option == 3:
            cp.eliminar_pelicula()

    except Exception as e:
        print(f'Ocurrio un error {e}')
        option = None
else:
    print('Termino de ejecutarse una pelicula   ')