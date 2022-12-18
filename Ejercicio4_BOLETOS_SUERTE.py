def luck_check(str):
    half = len(str) // 2
    if len(str) % 2 == 0:
        first_half = str[:half]
        second_half = str[half:]
    else:
        first_half = str[:half]
        second_half = str[half + 1:]

    return sum(int(x) for x in first_half) == sum(int(x) for x in second_half) 
    