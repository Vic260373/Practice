# Подключаем модули времени, даты и генератора случайных чисел.
import time
import datetime
import random

def gen_chislo(diap_min, diap_max): # Функция генератор чисел, получает два значения диапазона, начало и конец
    the_number = random.randint(diap_min, diap_max) # Используя эти значения генерирует случайное число.
    return the_number                               # Возвращает сгенерированное случайное число

def save_game(param):  # Функция принимает список параметров и сохраняет их в файл.
    with open("config.txt", "w") as conf:   # Открываем файл на запись, удаляя старые данные, если его нет создаем новый
        conf.writelines(f'{i} ' for i in param) # С помощью цикла записываем из списка поочередно параметры в файл.

def download_game():  # Функция загружает из файла параметры игры.
    param = []        # Создаем пустой список
    try:                                      # Делаем проверку
        with open("config.txt", "r") as conf: # Проверяем, существует ли файл.
            pass                              # Больше ничего не делаем
    except Exception:                         # Если файл не существует и проверка выдает исключение
        with open("config.txt", "w") as conf: # Создаем файл с именем config.txt.
            pass                              # Больше ничего не делаем
    with open("config.txt", "r") as conf: # Открываем файл на чтение
        for line in conf:                 # Считываем данные из файла
            for i in line.split():        # Делим данные по разделителю (пробелу) и поочередно с помощью цикла
                param.append(int(i))      # добавляем их в конец списка, преобразуя в целые числа
            return param                  # Возвращаем полученный список.

def statistic_game():                        # Функция выводит записи из файла статистики.
    try:                                            # Делаем проверку
        with open("statistics.txt", "r") as stat:   # Проверяем, существует ли файл, пытаясь отерыть его.
            pass                                    # Больше ничего не делаем
    except Exception:                               # Если файл не существует и проверка выдает исключение
        with open("statistics.txt", "w") as stat:   # Создаем файл с именем statistics.txt.
            pass                                    # Больше ничего не делаем
    with open("statistics.txt", "r") as stat:       # Открываем файл на чтение
        line = stat.read()                          # Считываем данные из файла
        if line == '':                              # Проверяем, если файл пустой,
            print('Нет сохраненных записей игры')   # выводим сообщение
        else:                                       # Если не пустой,
            print(line)                             # Выводим содержимое файла
            input('Нажмите Enter для продолжения...') # Ожидаем ввода для продолжения

def clear_statistic():                              # Функция удаляет данные в файле статистики.
    with open("statistics.txt", "w") as stat:       # Открываем файл в режиме записи, при этом все данные затираются.
        print('Статистика удалена')                 # Выводим сообщение.

def  save_statistic(start_time, end_time, tries):   # Функция принимает данные статистики и сохраняет их в файл.
    tries = str(tries)                              # Преобразуем переменную tries в строковую.
    sec = int(end_time - start_time)                # Расчитываем время игры в секундах.
    game_time = str(sec) + " сек "  # Формируем строку времени. Получаем строковое значение переменной sec и складываем строки.
    if sec > 60:                                    # Проверяем условие, если количество секунд > 60
        min = int(sec/60)                           # Находим количество минут.
        sec = sec % 60                              # Находим количество оставшихся секунд.
        game_time = str(min) + " мин " + str(sec) + " сек " # Формируем и перезаписываем строку времени с учетом минут.
        if min > 60:                                # Проверяем условие, если количество минут > 60
            hour = int(min/60)                      # Находим количество часов.
            min = min % 60                          # Находим количество оставшихся минут.
            game_time = str(hour) + " ч " + str(min) + " мин " + str(sec) + " сек " # Формируем и перезаписываем строку времени с учетом часов.
    now = datetime.datetime.now()                   # Получаем текущую дату
    now_time = str(now.strftime("%d-%m-%Y %H:%M"))  # Переводим дату в строку
    stat_add = now_time + "  Игра пройдена за " + game_time + " количество попыток " + tries # Формируем строку вывода
    try:                                            # Делаем проверку
        with open("statistics.txt", "r") as stat:   # Проверяем, существует ли файл, пытаясь отерыть его.
            pass                                    # Больше ничего не делаем
    except Exception:                               # Если файл не существует и проверка выдает исключение
        with open("statistics.txt", "w") as stat:   # Создаем файл с именем statistics.txt.
            pass                                    # Больше ничего не делаем
    with open('statistics.txt', 'a') as stat:       # Открываем файл с возможностьб дозаписи в конце файла.
        stat.write(stat_add + '\n')                 # Добавляем запись в файл

def choice():                                       # Функция проверки введенного символа с клавиатуры.
    res = False                                     # Определяем переменную res как логическую со значением False
    while res != True:                              # Запускаем цикл по условию, пока res не примет значение True
        simbol = input()                            # Ожидаем ввод символа с клавиатуры.
        if simbol == 'y' or simbol == 'q':          # Проверяем, является ли введенный символ 'y' или 'q'.
            return simbol                           # Если да, то возвращаем символ.
        else:                                       # Если нет
            print('Выберите "y" или "q"')           # Снова предлагаем выбрать символ 'y' или 'q'
            continue                                # Возвращаемся к началу цикла

def param_input():      # Функция позволяет изменить настройки игра.
    a = ['Введите начальное число диапазона ', 'Введите конечное число диапазона ',   # Создаем список
         'Введите количество возможных попыток, чтобы угадать число ']      # предложений.
    param = []                                      # Создаем пустой список.
    for i in range(3):                              # Создаем цикл на три итерации.
        res = False                                 # Определяем переменную res как логическую со значением False
        while res != True:                          # Запускаем цикл по условию, пока res не примет значение True
            print(a[i])                             # Выводим i-тый элемент списка 'a'
            chislo = input()                        # Ожидаем ввод числа с клавиатуры.
            chislo = test(chislo)                   # Передаем введенные символы для проверки в функцию test()
            if type(chislo) == int:                 # Проверяем, что возвращенное значение это число, а не символ 's'
                res = True                          # Если результат число, присваиваем переменной res значение True
                param.append(chislo)                # И добавляем это число в конец списка
    return param                                    # Возвращаем список с измененными настройками.

def help_game():                                    # Функция выводит помощь по игре.
    print(""" Игра - угадай число!
            Необходимо за минимальное количество попыток угадать загаданное число.
            Программа подсказывает больше или меньше искомое число.
            После пятой попытки, выходит подсказка, в каком диапазоне находится число.
            В меню выбора цифра 1 - запускает игру с настройками по умолчанию:
                Начальное число 1, конечное 100, количество попыток угадать - 10.
                Выбор цифры 2 - позволяет изменить количество попыток угадывания, а
                так же начальное и конечное значение диапазона загадываемого числа.
                Измененные настройки действуют пока программа запущена.
                Однако если выйти из программы и начать новую игру настройки сбрасываются.
                Настройки сохраняются вместе с игрой, при нажатии клавиши 's' во время игры.
                Если загрузить сохраненную игру, сохраненные настройки загрузятся с игрой.
                Клавиша 's' позволяет сохранить игру, во время угадывания и вернуться
                к ней позже. Для возврата к сохраненной игре надо в меню выбрать цифру - 3.
                Для просмотра статистики по играм надо выбрать цифру - 4.
                Цифра 5 служит для очистки статистики.
                Цифра 6 вызывает помощь по игре.
                Цифра 7 - выход из игры.             
                """)
    input('Для выхода нажмите Enter...')            # Ожидание нажатия клавиши Enter

def to_guess(diap_min, diap_max, max_tries, the_number, tries): # Функция угадывания числа, принимает 5 параиетров
    res = False                                     # Определяем переменную res как логическую со значением False
    par = False                                     # Определяем переменную par как логическую со значением False
    start_time = time.time()                        # Сохраняем текущее время начала игры с помощью функции time.time()
    while par != True:                              # Запускаем цикл по условию, пока par не примет значение True
        guess = test(input("Ваше предположение: \n"))   # Предлагаем ввести число и проверяем на валидность.
        if guess == 's':  # Проверка условия, что введен символ 's'
            print('Для сохранения прогресса игры надо сделать хотя бы одну попытку угадать')  # Выводим сообщение
            continue                                # Возврат к началу цикла.
        par = True                                  # Присваиваем переменной par значение True
    while guess != the_number or tries != max_tries: # В цикле сравниваем число с загаданным и количество сделанных попыток с максимальным
                                                    # В случае совпадения одного из значений цикл прекращает работу
        if guess > the_number:                      # Проверяем условие: Если введенное число > загаданного,
            print("Меньше...")                      # выводим "Меньше..."
        else:                                       # Иначе
            print("Больше...")                      # выводим "Больше..."
        print('Осталось попыток ', max_tries - tries) # Выводим количество оставшихся попыток.
        if tries == max_tries // 2:                 # Условие: Проверяем на достижение половины возможных попыток
            help_min = the_number - (the_number - diap_min) // 4    # Рассчитаваем диапазон подсказки, чтобы
            help_max = the_number + (diap_max - the_number) // 4    # его середина не являлась загаданным числом.
            print('Загаданное число находится в диаппазоне от ', help_min, ' до ', help_max) # Выводим подсказку.
        if tries == max_tries:                      # Проверка условия, что количество попыток достигло максимального
            print("\n Вы не уложились в заданное количество попыток", max_tries)    # Вывод оповещения
            print('Загаданное число ', the_number)  # Вывод загаданного числа
            break                                   # Прерывание цикла, выход из функции
        while res != True:                          # Запускаем цикл по условию, пока res не примет значение True
            guess = test(input("Ваше предположение: \n"))   # Предлагаем ввести число и проверяем на валидность.
            if guess == 's':                        # Проверка условия, что введен символ 's'
                param = [diap_min, diap_max, max_tries, the_number, tries] # Присваиваем значения списку 'param'
                save_game(param)                    # Передаем список 'param' в функцию save_game()
                print('Игра сохранена, чтобы продолжить игру нажмите "y", или чтобы выйти в меню "q" ') # Вывод сообщения
                simbol = choice()       # Запускаем функцию choice(), присваиваем возвращенное значение переменной simbol
                if simbol == 'q':                   # Проверяем условие, что выбран символ равен 'q'
                    return                          # Если да, выход из функции.
                continue                            # Если нет, возврат к началу цикла.
            break                                   # Прерываем выполнени цикла.
        tries += 1                                  # Увеличиваем счетчик попыток на единицу
        if guess == the_number:                     # Проверка на совпадение угаданного числа загаданному
            end_time = time.time()                  # В случае совпадения, сохраняем текущее время окончания игры
            save_statistic(start_time, end_time, tries) # Вызываем функцию сохранения статистики, передаем данные
            print("Поздравляю! Baм удалось отгадать число! Зто в самом деле", the_number)   # Выводим загаданное число
            print("Bы затратили попыток на отгадывание ", tries, " !\n")    # Выводим число попыток
            print("Для продолжения нажмите 'Enter' \n")                     # Предлагаем продолжить нажав Enter
            input()                                                         # Ожидание ввода
            break                                   # Прерываем работу функции to_guess()


def test(chislo):    # Функция проверяет введено число или символ 's', число проверяется на целое и положительное
    res = False                                     # Определяем переменную res как логическую со значением False
    while res != True:                              # Запускаем цикл по условию, пока res не примет значение True
        try:                                        # Делаем проверку,
            chislo = int(chislo)                    # что принятые символы - это число целое
        except Exception:                           # Если нет, возникает исключение
            if chislo == 's':                       # Проверяем на совпадение с символом 's'
                return chislo                       # Если да, то выходим из функции возвращая символ 's'
            else:                                   # Иначе,
                print("Это не целое число")         # Выводим сообщение
                chislo = input('Введите число \n')  # Просим ввести число, ожидаем ввода
                continue                            # Возвращаемся к началу цикла
        if chislo <= 0:                             # Проверяем условие, если число меньше или равно нулю
            print("Число должно быть положительное и больше 0") # Выводим сообщение
            chislo = input('Введите число \n')      # Просим ввести число, ожидаем ввода
            continue                                # Возвращаемся к началу цикла
        else:                                       # Иначе,
            res = True                              # Присваиваем переменной res значение True
    return chislo                                   # Выходим из функции возвращая проверенное число.


def menu():                                         # Функция Меню
    res = False                                     # Определяем переменную res как логическую со значением False
    while res != True:                              # Запускаем цикл по условию, пока res не примет значение True
        # Выводим Меню
        print(""" Выберите действие:
                    1. Начать играть.(Для сохранения, в игре нажмите 's')
                    2. Изменить настройки 
                    3. Загрузить игру
                    4. Посмотреть статистику
                    5. Очистить статистику
                    6. Помощь
                    7. Выход       """)

        choice = test(input())                      # Ввод значения, проверка с помощью функции test()
        if choice == 's':                           # Проверка на символ 's', если да, то
            print('Это не число')                   # вывод сообщения.
        else:                                       # Иначе,
            if choice > 0 and choice < 8:           # Проверка диапазона числа от 1 до 7, если да
                return choice                       # Выходим из функции возвращая проверенное число.
            else:                                   # Если нет,
                print('Нет такого пункта, попробуйте еще раз \n')   # Выводим сообщение

def main_game():                # Запуск игры начинается с этой функции
    diap_min = 1; diap_max = 100; max_tries = 10; tries = 1     # Задаем начальные значения
    res = False                                     # Определяем переменную res как логическую со значением False
    while res != True:                              # Запускаем цикл по условию, пока res не примет значение True
        choice = menu()                             # Вызываем функцию menu(), возвращенное значение присваиваем choice
        if choice == 1:                             # Проверяем условие, если переменная choice равна 1
            the_number = gen_chislo(diap_min, diap_max)     # От функции gen_chislo() получаем случайное число
            to_guess(diap_min, diap_max, max_tries, the_number, tries)  # Вызываем функцию to_guess() передавая параметры
        elif choice == 2:                           # Проверяем условие, если переменная choice равна 2
            par = False                             # Определяем переменную par как логическую со значением False
            while par != True:                      # Запускаем цикл по условию, пока par не примет значение True
                param = param_input()               # Вызываем функцию param_input(),и в возвращенном значении
                if param[0] >= param[1]:            # проверяем если начало больше или равно концу диапазона.
                    print('Конечное число диапазона не должно быть меньше или равно начальному.') # Выводим сообщение
                    continue                        # Возвращаемся к началу цикла
                par = True                          # Присваиваем переменной par значение True
            diap_min, diap_max, max_tries = param[0], param[1], param[2]    # Присваиваем значения переменным
            print('Настройки игры изменены')        # Выводим сообщение об изменении настроек.
        elif choice == 3:                           # Проверяем условие, если переменная choice равна 3
            param = download_game()                 # Вызываем функцию download_game()
            if param == None:                       # Если возвращенное значение равно None
                print('Нет сохраненных записей игры')   # Выводим сообщение
            # Присваиваем переменным значения из списка 'param'
            diap_min = param[0]; diap_max = param[1]; max_tries = param[2]; the_number = param[3]; tries = param[4]
            to_guess(diap_min, diap_max, max_tries, the_number, tries) # # Вызываем функцию to_guess() с 5 параметрами
        elif choice == 4:                           # Проверяем условие, если переменная choice равна 4
            statistic_game()                        # Вызываем функцию statistic_game()
        elif choice == 5:                           # Проверяем условие, если переменная choice равна 5
            clear_statistic()                       # Вызываем функцию clear_statistic()
        elif choice == 6:                           # Проверяем условие, если переменная choice равна 6
            help_game()                             # Вызываем функцию help_game()
        elif choice == 7:                           # Проверяем условие, если переменная choice равна 6
            break                                   # Выходим из функции, завершаем программу

print("\tДобро пожаловать в игру 'Отгадай число'!")                     # Выводим сообщение
print("\nЯ загадаю положительное натуральное число")                    # Выводим сообщение
print("А Вы постарайтесь отгадать его за минимальное число попыток.")   # Выводим сообщение
main_game()                                                             # Запускаем функцию  main_game()
