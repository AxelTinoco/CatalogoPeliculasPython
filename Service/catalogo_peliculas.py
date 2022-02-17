import os


class CatalogoPeliculas:
    ruta_archivo = 'peliculas.txt'

    @classmethod
    def agregar_pelicula(cls,pelicula):
        with open(cls.ruta_archivo,'a', encoding='utf8') as archivo:
            archivo.write(f'{pelicula.nombre} \n')


    @classmethod
    def listar_peliula(cls):
        with open(cls.ruta_archivo,'r',encoding='utf8') as archivo:
            print('Catalogo de peliculas'.center(50,'-'))
            print(archivo.read())

    @classmethod
    def eliminar_pelicula(cls):
        os.remove(cls.ruta_archivo)
        print(f'Se elimino la pelicula : {cls.ruta_archivo}')
