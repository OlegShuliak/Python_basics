# Дан список заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут только уникальные элементы исходного.

my_list_1 = [2, 2, 5, 12, 8, 2, 12]
result = []

for number in my_list_1:
    if my_list_1.count(number) == 1:
        result.append(number)

print(result)



