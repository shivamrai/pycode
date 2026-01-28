if __name__ == "__main__":
    lista = [7, 2, 4, 5, 1, 8]
    i = 0
    while i < len(lista):
        if i % 2 == 0:
            lista[i] *= lista[i]
        i += 1
    print(lista)
