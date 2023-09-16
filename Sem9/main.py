import sys
from core import create_folder, create_file, get_list, delete_file, copy_file, save_info, change_dir
from game_guess_num_rev import game_guess_num_rev
from  game_guess_num import game_guess_num

save_info('Старт')

try:
    command = sys.argv[1]
except IndexError:
    print('Необходимо выбрать команду. help')
else:
    if command == 'list':
        get_list()
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название файла')
        else:
            create_file(name)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Необходимо ввести имя папки')
        else:
            create_folder(name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Необходимо ввести имя папки (файла)')
        else:
            delete_file(name)
    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError:
            print('Необходимо ввести низвание файла и название копии')
        else:
            copy_file(name, new_name)
    elif command == 'change':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Необходимо ввести имя папки')
        else:
            change_dir(name)
    elif command == 'reverse':
        game_guess_num_rev()
    elif command == 'game':
        game_guess_num()
    elif command == 'help':
        print('list - список файлов и папок')
        print('create_file- создание файла')
        print('create_folder - создание папки')
        print('delete - удаление файла или папки')
        print('change - изменение рабочей папки')
        print('reverse - игра "Угадай число наоборот"')
        print('game - игра "Угадай число"')
        print('copy - копирование файла или папки')

    save_info('Конец')
