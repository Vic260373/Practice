import math

def test():
    res = False
    while res != True:
        a = input('Введите положительное целое число \n')
        try:
            a = int(a)
        except Exception:
            print( "Это не целое число")
            continue
        if a <= 0:
            print("Число должно быть положительное и больше 0")
        else:
            return math.factorial(a)

print('Программа расчета факториала числа \n')

print('Ответ \n', test())


