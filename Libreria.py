

class Libro:
    def __init__(self, codigo_ISBN = '', titulo = '', genero = 0, idioma = 0, precio = 0.0):
        self.codigo_ISBN = codigo_ISBN
        self.titulo = titulo
        self.genero = genero
        self.idioma = idioma
        self.precio = precio


# Muestra el libro con los idiomas y generos en palabras y no en codigos
def to_string(libro):
    genero = ['Autoayuda', 'Arte', 'Ficción', 'Computacion', 'Economía', 'Escolar', 'Sociedad', 'Gastronomía', 'Infantil', 'Otros']
    idioma = ['Español', 'Inglés', 'Francés', 'Italiano', 'Otros']
    cadena = ''
    cadena += '{:<10}'.format(' identificacion: ' + str(libro.codigo_ISBN) + '\t')
    cadena += '{:<10}'.format('| titulo: ' + libro.titulo + '\t')
    cadena += '{:<10}'.format('| genero: ' + genero[libro.genero] + '\t')
    cadena += '{:<10}'.format('| idioma: ' + idioma[libro.idioma - 1] + '\t')
    cadena += '{:<10}'.format('| precio: ' + str(libro.precio) + '\t')

    return cadena


# Muestra los libros pero con los codigos en idioma y genero
def write(libro):
    cadena = ''
    cadena += '{:<10}'.format(' identificacion: ' + str(libro.codigo_ISBN) + '\t')
    cadena += '{:<10}'.format('| titulo: ' + libro.titulo + '\t')
    cadena += '{:<10}'.format('| genero: ' + str(libro.genero) + '\t')
    cadena += '{:<10}'.format('| idioma: ' + str(libro.idioma) + '\t')
    cadena += '{:<10}'.format('| precio: ' + str(libro.precio) + '\t')

    return cadena


def test():
    lib = Libro(159159, "Harry Explorer", 5, 2, 500)

    print(to_string(lib))
    print("-"*40)
    write(lib)


if __name__ == '__main__':
    test()
