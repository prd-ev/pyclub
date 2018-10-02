def generator():
    lista = []
    numer = int(input("Podaj numer"))
    while numer >= 0:
        lista.append(numer)
        numer -= 1
    return lista
