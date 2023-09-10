# Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health = 100,
# damage = 50.
### Поэкспериментируйте с значениями урона и жизней по желанию.
### Теперь надо создать функцию attack(person1, person2). Примечание: имена аргументов можете указать свои.
### Функция в качестве аргумента будет принимать атакующего и атакуемого.
### В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого.
# Функция должна сама работать со словарями и изменять их значения.


name_1 = input('Введите имя 1-го персонажа: \n')
name_2 = input('Введите имя 2-го персонажа: \n')

player_1 = {'name': name_1, 'health': 100, 'damage': 50}
player_2 = {'name': name_2, 'health': 100, 'damage': 50}

print(player_1)
print(player_2)


def attack(attack_player, attacked_player):
    attacked_player['health'] = attacked_player['health'] - attack_player['damage']
    return attacked_player


attack(player_1, player_2)

print(player_1)
print(player_2)
