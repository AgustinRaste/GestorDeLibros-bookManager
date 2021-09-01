# En este modulo se generan los codigos isbn, el metodo para crearlos es escribir un numero al azar
# pero con 9 digitos, calcular el mod de la suma como indica el metodo para validar un ISBN y una vez que se
# obtiene el mod,  se le agrega un digito con el valor que haga falta para que la suma final sea divisibble por 11



# esta funcion es la que agrega el ultimo caracter
def probarCodigo(codigo):
    acum = 0
    contadorGuion = 0
    aux = 10
    for i in range(len(codigo)):
        if codigo[i] == '-':
            contadorGuion += 1
            continue
        else:
            print(codigo[i], "x", aux)
            cod = int(codigo[i])
            cod *= aux
            acum += cod
            aux -= 1
    print(acum % 11)
    # en el return obtengo el codigo agregando por concatenacion ell digito que le falta para ser divisible por 11
    return codigo + str(11 - (acum % 11))

# esta funcion es la que sirve para validar un codigo y determinar que cumpla con las condiciones de un Isbn

def validarCodigo(codigo):
    acum = 0
    contadorGuion = 0
    aux = 10
    for i in range(len(codigo)):
        if codigo[i] == '-':
            contadorGuion += 1
            continue
        else:
            cod = int(codigo[i])
            cod *= aux
            acum += cod
            aux -= 1

    if (contadorGuion == 3) and (acum % 11 == 0):
        # Codigo Valido
        return codigo
    else:
        # Codigo no valido
        # Si no es valido me devuelve un -1
        return -1


# En esta funcion lo que se hace es verificar que no haya ningun isbn repetido en
# todo el array que se armó con los codigos

def buscarIguales(array):
    hayigual = False
    for j in range(len(array)):
        aux = array[j]
        for p in range(len(array)):
            if aux == array[p]:
                if p == j:
                    continue
                else:
                    hayigual = True
    if not hayigual:
        print("son todos diferentes")

    # Retorna True si hay dos o mas codigos iguales y False si son todos diferentes
    return hayigual

def test():
    #El array fue cargado con los codigos que fui generando con la funcion probarCodig()
    array = ['848-88-326-56', '84-818-326-85', '25-8887-32-78', '951-635-52-18', '789-52-78-118', '8956-852-4-72', '785-258-5-817', '147-258-336-1', '854-87-951-23', '785-963-5-895', '7-8524-63-207', '85-7193-65-01', '2356-785-4-85', '159-753-5-729', '12-8511-72-12', '39-3549-01-51', '1-2020-544-39', '85-633-541-59', '75-643-591-53', '8524-668-12-1', '854-6925-75-5', '254-66-852-28', '4144-706-52-4', '2356-1-8025-7', '23-56-89-5213', '753-951-52-28', '145-2-5894-53', '222-652-114-3', '417-236-655-4', '258-4-1522-66', '159-853-5-722', '3224-85-4-766']

    for i in range(len(array)):
        if validarCodigo(array[i]) == -1:
            print("El codigo no es valido")
        else:
            print("El codigo es valido")

    if buscarIguales(array):
        print("Hay codigos iguales")
    else:
        print("Son todos diferentes, el array esta Ok")

    print(array)
# LISTADO DE CODIGOS GENERADOS

# 1| 848-88-326-56
# 2| 84-818-326-85
# 3| 25-8887-32-78
# 4| 951-635-52-18
# 5| 789-52-78-118
# 6| 8956-852-4-72
# 7| 785-258-5-817
# 8| 147-258-336-1
# 9| 854-87-951-23
# 10| 785-963-5-895
# 11| 7-8524-63-207
# 12| 85-7193-65-01
# 13| 2356-785-4-85
# 14| 159-753-5-729
# 15| 12-8511-72-12
# 16| 39-3549-01-51
# 17| 1-2020-544-39
# 18| 85-633-541-59
# 19| 75-643-591-53
# 20| 8524-668-12-1
# 21| 854-6925-75-5
# 22| 254-66-852-28
# 23| 4144-706-52-4
# 24| 2356-1-8025-7
# 25| 23-56-89-5213
# 26| 753-951-52-28
# 27| 145-2-5894-53
# 28| 222-652-114-3
# 29| 417-236-655-4
# 30| 258-4-1522-66
# 31| 159-853-5-722
# 32| 3224-85-4-766

if __name__ == '__main__':
    test()
