# Создайте функцию, принимающую на вход имя, возраст и город проживания человека.
# Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва»

name = 'Василий'
age = 21
city = 'Москва'

def get_info(name, age, city):
    return str(f'{name}, {age} год(а), проживает в городе {city}')

print(get_info(name, age, city))