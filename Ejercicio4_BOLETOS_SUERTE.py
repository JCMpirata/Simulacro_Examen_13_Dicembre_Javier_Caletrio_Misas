def luck_check(str):
    half = len(str) // 2
    if len(str) % 2 == 0:
        first_half = str[:half]
        second_half = str[half:]
    else:
        first_half = str[:half]
        second_half = str[half + 1:]

    return sum(int(x) for x in first_half) == sum(int(x) for x in second_half)

if __name__ == '__main__':
    print(luck_check('123321'))
    print(luck_check('12321'))
    print(luck_check('12345'))
    print(luck_check('123456'))
    print(luck_check('1234567'))
    
