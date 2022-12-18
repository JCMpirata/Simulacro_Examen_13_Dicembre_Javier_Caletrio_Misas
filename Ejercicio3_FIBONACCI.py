def Fibonacci(num: int):
    lista = []
    num = _fibonacci(lista, 0, num)
    return lista[-1]

def _fibonacci(lista: list, start: int, end: int):
    if start == 0 or start == 1:
        lista.append(start)

    elif 1 < start < end:
        lista.append(lista[-1] + lista[-2])
    
    else:
        return lista[-1]

    return _fibonacci(lista, start + 1, end)





    

