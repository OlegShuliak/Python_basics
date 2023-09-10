# Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.

num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

def max_num(num_1, num_2, num_3):
    return max(num_1, num_2, num_3)

print(max_num(num_1, num_2, num_3))