def luck_check(str):
    half = len(str) // 2
    if len(str) % 2 == 0:
        first_half = str[:half]
        second_half = str[half:]
    else:
        first_half = str[:half]
        second_half = str[half + 1:]
        