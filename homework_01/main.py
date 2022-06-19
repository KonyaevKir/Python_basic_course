"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    return [number ** 2 for number in numbers]

"""
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
"""


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(num):
    # if num is None:
    #     return False
    for n in range(2,int(num ** 0.5) + 1):
        if num % n == 0:
            return False
    return True

def filter_numbers(numbers_lst, filter_type):
    if filter_type == ODD:
        return [num for num in numbers_lst if num % 2]
    if filter_type == EVEN:
        return [num for num in numbers_lst if num % 2 == 0]
    if filter_type == PRIME:
        return [num for num in numbers_lst if is_prime(num)]

"""
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
"""
