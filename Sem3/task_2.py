# Дана дата в формате dd.mm.yyyy, например: 02.11.2013. Ваша задача — вывести дату в текстовом виде, например:
# второе ноября 2013 года. Склонением пренебречь (2000 года, 2010 года)


date = input('Введите дату в формате dd.mm.yyyy:\n')

day = {'01': 'первое', '02': 'второе', '03': 'третье', '04': 'четвертое', '05': 'пятое', '06': 'шестое',
       '07': 'седьмое', '08': 'восьмое', '09': 'девятое', '10': 'десятое',
       '11': 'одиннадцатое', '12': 'двенадцатое', '13': 'тринадцатое', '14': 'четырнадцатое', '15': 'пятнадцатое',
       '16': 'шеснадцатое', '17': 'семнадцатое', '18': 'восемнадцатое', '19': 'девятнадцатое', '20': 'двадцатое',
       '21': 'двадцать первое', '22': 'двадцать второе', '23': 'двадцать третье', '24': 'двадцать четвертое',
       '25': 'двадцать пятое', '26': 'двадцать шестое', '27': 'двадцать седьмое', '28': 'двадцать восьмое',
       '29': 'двадцать девятое', '30': 'тридцатое',
       '31': 'тридцать первое'}

month = {'01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля', '05': 'мая', '06': 'июня',
         '07': 'июля', '08': 'августа', '09': 'сентября', '10': 'октября',
         '11': 'ноября', '12': 'декабря'}

print('{} {} {} года'.format(day[date[0:2]], month[date[3:5]], date[6:]))

