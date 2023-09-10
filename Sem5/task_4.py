# Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр - armor = 1.2 (величина брони персонажа)
# Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно, у вас должно быть 2 функции:
# Наносит урон. Это улучшенная версия функции из задачи 3.
# Вычисляет урон по отношению к броне.

name_1 = input('Введите имя 1-го персонажа: \n')
name_2 = input('Введите имя 2-го персонажа: \n')

player_1 = {'name': name_1, 'health': 100, 'damage': 50, 'armor': 1.2}
player_2 = {'name': name_2, 'health': 100, 'damage': 50, 'armor': 1.5}

print(player_1)
print(player_2)

def damage(attack_player, attacked_player):
    return int(attack_player['damage']/attacked_player['armor'])

def attack(attack_player, attacked_player, damage):
    attacked_player['health'] = attacked_player['health'] - damage(attack_player, attacked_player)
    return attacked_player


attack(player_1, player_2, damage)

print(player_1)
print(player_2)