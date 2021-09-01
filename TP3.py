import Libreria
import generarIsbn as isbn
import random
__author__ = 'Agustin Rastellini'


print('-'*117)
print('\t\t\t\ttp3 - SISTEMA DE GESTION PARA TIENDA DE LIBROS ELECTRONICOS')
print('-'*117)
# una tienda de libros electronicos nos solicita ayuda para desarrollar un sistema de gestion de sus productos.
# de cada libro se conoce:

# . codigo de identificacion o ISBN (cadena de caracteres)
# . titulo
# . genero (0: autoayuda, 1: arte, 2: ficcion, 3: computacion, 4: economia, 5: escolar, 6: sociedad, 7: gastronomia,
#           8: infantil, 9: otros)
# . idioma (1: español, 2: ingles, 3: frances, 4: italiano, 5: otros)
# . precio

# se solicita un programa controlado por menu de opciones que permita lo siguiente:

# 1.) generacion y carga: generar un arreglo unidimensional con los n libros que ofrece la libreria (n es un valor que se
#     ingresa por teclado).Para el presente practico se solicita que el usuario pueda optar por una carga manual (validar
#     los datos de entrada) o por una carga automatica de los datos de cada libro.

#     Se debe tener en cuenta que el international standard book number (ISBN) es un identificador unico para libros creado
#     para uso comercial.Se creo en 1966 en el reino unido y alcanzo el rango de estandar internacional en 1970.Todas las
#     ediciones y variaciones de un libro reciben un ISBN de 10 digitos en los cuatro grupos que se indican a continuacion
#     (sin longitud fija por cada grupo) separados por guiones ("-"):

#     a. codigo de pais o lengua de origen.
#     b. codigo del editor (asignado por la agencia nacional del ISBN)
#     c. numero del articulo (elegido por el editor)
#     d. digito de control

# se sabe que sus digitos x1,x2,x3,...,x10 satisfacen la relacion:
#     (10x1 + 9x2 + 8x3 + 7x4 + 6x5 + 5x6 + 4x7 + 3x8 + 2x9 + x10)mod11 = 0

# en definitiva,el resto de dividir esa suma por 11,debe dar cero.Por ejemplo,para el siguiente ISBN:
# 84-8181-227-7 se comprueba que: 10*8+9*4+8*8+7*1+6*8+5*1+4*2+3*2+2*7+7 = 275 y al dividir 275 por 11 vemos que el resto
# es 0.Lo que nos indica que es un ISBN valido (275 % 11 = 0).

# . el siguiente ISBN 5555687-525 no es valido porque no tiene los 4 grupos.
# . el ISBN 456--55-25438 tiene los 10 digitos,y la cantidad de guiones correcta pero no tiene los 4 grupos dado que hay
#   dos guiones seguidos.
# . para el ISBN 451-567-43-89 se comprueba que:
#   10*4+9*5+8*1+7*5+6*6+5*7+4*4+3*3+2*8+9 = 249 y al dividir por 11 el resto no es cero,lo que nos indica que no es un
#   ISBN valido.

# 2.) Mostrar: mostrar el vector generado en el punto anterior de tal manera que se muestre el genero y el idioma del libro
#     en lugar de los numeros que los representan y se listen ordenados por titulo en forma ascendente.Cada libro debe mostrarse
#     a razon de una linea por registro.

# 3.) Conteo y genero mas popular: determinar la cantidad de libros ofrecidos por genero.mostrar dichas cantidades y el genero
#     al que corresponde mostrando su nombre y no su codigo. Determinar el genero con mayor cantidad de libros ofrecidos,
#     indicando su nombre.Si hubiera mas de un genero con la misma cantidad,informar uno solo.

# 4.) Busqueda del mayor: Determinar y mostrar el libro de mayor precio para un idioma i,siendo i un valor que se ingresa
#     por teclado.Si existiera mas de un libro con el mismo mayor precio mostrar solo uno.

# 5.) Busqueda por ISBN: Buscar si en el vector existe un libro con el ISBN x,siendo x un valor que se ingrese por teclado.
#     Si existe mostrar sus datos y aumentar su precio un 10%.Si no existe,mostrar un mensaje por pantalla.

# 6.) Consulta de un genero: Mostrar los datos de los libros del genero con mayor cantidad de libros identificado en el punto 3
#     Dicho listado debe mostrarse ordenado por precio de mayor a menor.

# 7.) Consulta de precio por grupo: Esta funcionalidad perminte a los alumnos secundarios cargar el listado de los ISBN
#     correspondientes a los libros que el colegio les exige para el año escolar.El sistema debe buscar cuales de estos
#     libros se encuentran en su catalogo e indicar:

#    a. Los libros que no se encontraron en el catalogo.
#    b. Los libros que si se encontraron en el catalogo con su precio.

# El precio total que el estudiante deberia pagar para comprar aquellos libros que la libreria vende.


def validar(inf):
    numero = int(input('ingresa un numero (mayor a ' + str(inf) + '): '))
    while numero <= inf:
        numero = int(input('error: tiene que ser mayor a ' + str(inf) + ' carga de nuevo:'))
    return numero


def validar_entre(inf, sup, mensaje):
    carga = int(input(mensaje))
    while carga < inf or carga > sup:
        carga = int(input('Error: la carga tiene que ser ' + mensaje + ' carga de nuevo:'))
    return carga


def read_manual(arrLibros):
    tamaño = len(arrLibros)
    for i in range(tamaño):

        codigo_ISBN = input("Ingrese un codigo ISBN")
        # validacion de codigo
        while isbn.validarCodigo(codigo_ISBN) == -1:
            codigo_ISBN = input("CODIGO INVALIDO! Ingrese nuevamente el codigo ISBN:")

        titulo = input('ingresa el titulo del libro')
        genero = validar_entre(0, 9, 'Ingresa el genero del libro: ')
        idioma = validar_entre(1, 5, 'ingresa el idioma del libro: ')
        precio = validar_entre(0, 10000, 'Ingresa el precio del libro: ')

        arrLibros[i] = Libreria.Libro(codigo_ISBN, titulo, genero, idioma, precio)
    return arrLibros


def read_automatico(arrLibros):
    arrayIsbn = ['848-88-326-56', '84-818-326-85', '25-8887-32-78', '951-635-52-18', '789-52-78-118', '8956-852-4-72', '785-258-5-817', '147-258-336-1', '854-87-951-23', '785-963-5-895', '7-8524-63-207', '85-7193-65-01', '2356-785-4-85', '159-753-5-729', '12-8511-72-12', '39-3549-01-51', '1-2020-544-39', '85-633-541-59', '75-643-591-53', '8524-668-12-1', '854-6925-75-5', '254-66-852-28', '4144-706-52-4', '2356-1-8025-7', '23-56-89-5213', '753-951-52-28', '145-2-5894-53', '222-652-114-3', '417-236-655-4', '258-4-1522-66', '159-853-5-722', '3224-85-4-766']

    stock = ['O(n) y su familia', 'AED for dummies', 'Puntero y yo', 'La otra cara del print', '2B or not 2B', 'El ladron de referencias', 'Recursion y recursado']
    tamaño = len(arrLibros)
    for i in range(tamaño):
        codigo_ISBN = random.choice(arrayIsbn)
        arrayIsbn.remove(codigo_ISBN)
        # agregando los metodos remove me aseguro de que no se repitan los valores, ya que
        # luego de asignarlo lo elimina de las posibilidades para la proxima asignacion
        titulo = random.choice(stock)
        genero = random.randint(0, 9)
        idioma = random.randint(0, 5)
        precio = random.randint(1, 999)
        arrLibros[i] = Libreria.Libro(codigo_ISBN, titulo, genero, idioma, precio)

    return arrLibros


def mostrarLibros(arrLibros):
    for libro in arrLibros:
        print(Libreria.to_string(libro))


def opcionDeCarga():
    return validar_entre(1, 2, '[Carga manual(1) - Carga automatica(2)] ')


def ordernarTitulo(arrLibros):
    # Algoritmo de ordenamiento
    n = len(arrLibros)
    for i in range(n-1):
        for j in range(i+1, n):
            if arrLibros[i].titulo > arrLibros[j].titulo:
                arrLibros[i], arrLibros[j] = arrLibros[j], arrLibros[i]


def ordernarPrecio(arrLibros):
    # Algoritmo de ordenamiento
    n = len(arrLibros)
    for i in range(n-1):
        for j in range(i+1, n):
            if arrLibros[i].precio < arrLibros[j].precio:
                arrLibros[i], arrLibros[j] = arrLibros[j], arrLibros[i]


def contarGenero(arrLibros):
    arrCont = [0] * 10
    for i in range(len(arrLibros)):
        ind = arrLibros[i].genero
        arrCont[ind] += 1
    return arrCont


def mostrarConteoGenero(arrConteo):
    genero = ['Autoayuda', 'Arte', 'Ficción', 'Computacion', 'Economía', 'Escolar', 'Sociedad', 'Gastronomía', 'Infantil', 'Otros']
    print("Cantidad de libros por genero: ")
    for i in range(len(arrConteo)):
        print(genero[i], ": ", arrConteo[i])


# Esta funcion me devuelve un str con el genero que mas cantidad tiene
def buscarMayorCantGenero(arrConteo):
    genero = ['Autoayuda', 'Arte', 'Ficción', 'Computacion', 'Economía', 'Escolar', 'Sociedad', 'Gastronomía', 'Infantil', 'Otros']
    mayCantGenero = 0
    indMayCantGenero = 0
    for i in range(len(arrConteo)):
        if arrConteo[i] > mayCantGenero:
            mayCantGenero = arrConteo[i]
            indMayCantGenero = i

    return genero[indMayCantGenero]


def buscarLibroIdioma_MayorPrecio(arrLibros, idioma):
    encontrado = False
    arrUnIdioma = []
    # print("prueba de idioma en un libro: ", arrLibros[15].idioma)
    # print(type(idioma))
    # print(type(arrLibros[15].idioma))

    for i in range(len(arrLibros)):
        if arrLibros[i].idioma == int(idioma):
            arrUnIdioma.append(arrLibros[i])
            # write(arrLibros[i])
            encontrado = True
    id = buscarMayorPrecio(arrUnIdioma)

    if encontrado == False:
        print('Libro Inexistente ...')
    else:
        return arrUnIdioma[id]


def buscarMayorPrecio(arrLibros):
    indice = 0
    mayPrecio = 0
    for i in range(len(arrLibros)):
        if arrLibros[i].precio > mayPrecio:
            mayPrecio = arrLibros[i].precio
            indice = i

    return indice


# Al llamar la funcion se debe indicar True o False en el aprametro aumentar para que se le aplique el aumento del 10% a la busqueda
def buscarPorISBN(arrLibros, cod, aumentar):
    ban = False
    for i in range(len(arrLibros)):
        if arrLibros[i].codigo_ISBN == cod:
            libroEncontrado = arrLibros[i]
            # print(Libreria.to_string(arrLibros[i]))
            ban = True
            print("1 repeticion")
    if aumentar:
        libroEncontrado.precio += 1.1
    if ban == False:
        return -1
    else:
        return libroEncontrado


# Me devuelve un array con libros encontrados
def buscarPorGenero(arrLibros, gen):
    ban = False
    encontrados = []

    for i in range(len(arrLibros)):
        if arrLibros[i].genero == gen:
            encontrados.append(arrLibros[i])
            ban = True

    if ban == False:
        print('Libro Inexistente ...')
    else:
        mostrarLibros(encontrados)
        print("_"*60)
        return encontrados


def codificarGenero(gen):
    genero = ['Autoayuda', 'Arte', 'Ficción', 'Computacion', 'Economía', 'Escolar', 'Sociedad', 'Gastronomía', 'Infantil', 'Otros']
    for i in range(len(genero)):
        if gen == genero[i]:
            codigoGenero = i

    return codigoGenero


def principal():
    # Limitamos la cantidad posible a 32 por ser los isbn que tenemos disponibles (principalmente para la carga automatica)
    # ya que, de ser un numero mayor, se repètirian los isbn
    libros = []
    opcion = -1

    while opcion != 0:

        print('\n=== MENU DE OPCIONES ===\n'
              '1. generacion y carga\n'
              '2. mostrar\n'
              '3. Conteo y genero mas popular\n'
              '4. Busqueda del mayor precio segun un idioma\n'
              '5. Busqueda por ISBN\n'
              '6. Consulta de un genero\n'
              '7. Consulta de precio por grupo\n'
              '0. salir\n')
        print()
        opcion = int(input('ingresa la opcion que quieras: '))
        print()

        # Determinacion de las acciones de cada opcion
        if opcion == 1:
            print("Carga de libros")
            n = int(validar_entre(0, 32, 'Ingrese la cantidad de libros a cargar (entre 0 y 32): '))
            libros = [None] * n
            carga = opcionDeCarga()
            if carga == 1:
                libros = read_manual(libros)
                # mostrarLibros(libros)
            elif carga == 2:
                libros = read_automatico(libros)
                # mostrarLibros(libros)
            print("Arreglo cargado con ", n," libros!")

        elif opcion == 2:
            if len(libros) == 0:
                print("Aun no se cargó ningun libro!")
            else:
                print("Listado de libros cargados: ")
                ordernarTitulo(libros)
                mostrarLibros(libros)

        elif opcion == 3:
            if len(libros) == 0:
                print("Aun no se cargó ningun libro!")
            else:
                print("Mostrar cantidad de libros por género")
                arrContGeneros = contarGenero(libros)
                mostrarConteoGenero(arrContGeneros)

                mayGenero = buscarMayorCantGenero(arrContGeneros)
                print("El genero que mas cantidad de libros tiene es: ", mayGenero)

        elif opcion == 4:
            if len(libros) == 0:
                print("Aun no se cargó ningun libro!")
            else:
                print("Busqueda de mayor precio de libro segun un idioma ingresado")
                for j in range(len(libros)):
                    print(Libreria.write(libros[j]))
                print("Opciones de busqueda de idiomas: \n")
                print("1 - Español \n"
                      "2 - Inglés \n"
                      "3 - Francés \n"
                      "4 - Italiano \n"
                      "5 - Otros \n")
                i = input("Ingrese el idioma que desea buscar: ")
                lib = buscarLibroIdioma_MayorPrecio(libros, i)
                print("Libro encontrado: ", lib.titulo)
                print("Precio: ", lib.precio)

        elif opcion == 5:
            if len(libros) == 0:
                print("Aun no se cargó ningun libro!")
            else:
                print("Busqueda de un libro por ISBN: ")
                cod = input("Ingrese el codigo ISBN que desea buscar: ")

                while isbn.validarCodigo(cod) == -1:
                    cod = input("CODIGO INVALIDO! Ingrese nuevamente el codigo ISBN: ")

                lib = buscarPorISBN(libros, cod, True)
                if lib != -1:
                    print(Libreria.write(lib))
                else:
                    print("El libro no fue encontrado")

        elif opcion == 6:
            if len(libros) == 0:
                print("Aun no se cargó ningun libro!")
            else:

# los libros estan cargados con codigos en el genero, por lo tanto
# asignamos el codigo segun el genero que mas cantidad tiene

                genero = codificarGenero(mayGenero)
                print(mayGenero)
                librosGenero = buscarPorGenero(libros, genero)
                ordernarPrecio(librosGenero)
                mostrarLibros(librosGenero)

        elif opcion == 7:
            acumPrecio = 0
            encontrados = []
            if len(libros) == 0:
                print("Aun no se cargó ningun libro!")
            else:
                print("Averiguar existencia y precio de un grupo de codigos: ")
                print("Ingrese los codigos ISBN que desea buscar, con -1 corta: ")
                arrCod = []
                cod = input("Ingrese un codigo: ")
                while cod != '-1':
                    if cod != '-1':
                        while isbn.validarCodigo(cod) == -1:
                            cod = input("CODIGO INVALIDO! Ingrese nuevamente el codigo ISBN:")
                            if cod == -1:
                                # Aplico esta instruccion para que no me tome el -1 como un codigo invalido
                                continue
                    arrCod.append(cod)
                    cod = input("Ingrese otro codigo o -1 para terminar: ")

                # en arrCod tengo todos los codigos que se desean buscar

                for i in range(len(arrCod)):
                    encontrado = buscarPorISBN(libros, arrCod[i], False)
                    if encontrado == -1:
                        print("-" * 60)
                        print("El codigo ", arrCod[i], "no fue encontrado")
                    else:
                        print("-" * 60)
                        print("El codigo ", arrCod[i], "fue encontrado")
                        print("Pertenece al libro ", encontrado.titulo)
                        print("Su precio es de $", round(encontrado.precio,2))

                        encontrados.append(encontrado)

                for i in range(len(encontrados)):
                    acumPrecio += encontrados[i].precio
                print("El alumno debe pagar un total de: ", round(acumPrecio, 2))

        else:
            if opcion != 0:
                print('opcion no valida')

    print("Saliendo del programa")

if __name__ == '__main__':
    principal()
