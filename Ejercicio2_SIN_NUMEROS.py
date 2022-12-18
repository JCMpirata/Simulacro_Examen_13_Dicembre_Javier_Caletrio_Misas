def sin_numeros(cadena):
    assert(type(cadena) == str)
    return "Puedo escribir numeros como " + cadena

if __name__ == '__main__':
    print(sin_numeros("1, 2, 3"))
