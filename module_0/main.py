import numpy as np


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return (score)


def create_range(minimum, maximum):
    return range(minimum, maximum + 1)


def check_predict(number: int, search_range: list):
    '''Метод для проверки числа, получает число и список вариантов.
        Если число не подходит, сокращает список вариантов
        Если число угадано, возвращает True'''
    minimum = search_range[0]
    maximum = search_range[1]
    predict = np.random.randint(minimum, maximum)
    if number != predict:
        if number > predict:
            return [predict, maximum+1]
        elif number < predict:
            return [minimum, predict+1]
    else:
        return True


def game_core_v2(number: int):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    search_range = [1, 101]
    while True:
        search_range = check_predict(number, search_range)
        if search_range == True:
            return(count)    # выход из цикла, если угадали
        count += 1
        if count > 101:  # выход из цикла, если что-то пошло не так
            return 'Никогда'


score_game(game_core_v2)
