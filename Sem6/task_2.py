# Создайте модуль. В нем создайте функцию, которая принимает список и возвращает из него случайный элемент.
# Если список пустой функция должна вернуть None. Проверьте работу функций в этом же модуле.
#     Примечание: Список для проверки введите вручную. Или возьмите этот: [1, 2, 3, 4]

import random


def get_element(elements):
    if len(elements) != 0:
        return random.choice(elements)


if __name__ == '__main__':
    elements = [1, 2, 3, 4]
    elements_none = []
    print(get_element(elements))
