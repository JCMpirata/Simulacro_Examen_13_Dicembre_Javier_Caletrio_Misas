def checkio(text: str) -> list:
    lista = []
    for i in text.split():
        if i.startswith("#"):
            lista.append(i.replace("#", ""))

    return lista

if __name__ == '__main__':
    print(checkio("#AVATAR #2 EL #SENTIDO DEL #AGUA"))