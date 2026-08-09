from pathlib import Path
from game import Game
from clear_screen import clear_screen
from selection_menu import selection_menu
import json


def menu():
    while True:
        clear_screen()
        print('\n----- МЕНЮ -----')
        choice = input('0 - начать\n1 - выйти\n2 - доп.информация\n3 - мои рекорды\nВыбери действие: ')

        if choice == '0':
            selection_menu()

        elif choice == '1':
            break

        elif choice == '2':
            clear_screen()
            print('-' * 30)
            print(f'Это игра RandGame, а точнее игра угадай число. Чтобы начать игру выбери нужное действие в меню.\nДалее игра сама начнется и тебе нужно просто отгадывать числа.\nПриятной игры!')
            print('-' * 30)
            input('Enter - чтобы выйти: ')

        elif choice == '3':
            clear_screen()
            path = Path('record.json')
            try:
                contents = path.read_text()
                record = json.loads(contents)
            except FileNotFoundError:
                print('Рекордов пока нет! Сыграйте хотя бы раз, что бы они появились здесь.')
                input('Enter - чтобы выйти: ')

            print(f'Ваши рекорды:\nЛегкий режим: {record['easy']} попыток.\nНормальный режим: {record['normal']} попыток.\nСложный режим: {record['hard']} попыток.')
            input('Enter - чтобы выйти: ')
        else:
            print(f'Ошибка! Действия "{choice}" не существует. Выберите существующие действие.')
            input('Enter - чтобы продолжить: ')
            continue
