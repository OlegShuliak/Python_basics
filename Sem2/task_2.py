# Используя цикл, запрашивайте у пользователя число, пока оно не станет больше 0, но меньше 10.
# После того, как пользователь введет корректное число, возведите его в степень 2 и выведите на экран.
# Например, пользователь вводит число 123, вы сообщаете ему, что число неверное, и говорите о диапазоне допустимых. И просите ввести заново.
# Допустим, пользователь ввел 2, оно подходит. Возводим его в степень 2 и выводим 4.


while True:
    number = input('Введите число\n')
    if 0 < int(number) < 10:
        number = int(number) ** 2
        print(number)
        break
    else:
        print('Неверное число, число должно быть больше 0 и меньше 10. Повторите попытку ввода:\n')