from game import Game
from clear_screen import clear_screen

def selection_menu():
    while True:
        clear_screen()
        print('----- ВЫБОР РЕЖИМА СЛОЖНОСТИ -----')
        choice_game = input('0 - легкий\n1 - нормальный\n2 - сложный\n3 - выйти в главное меню\nВыбери действие: ')

        if choice_game == '0':
            clear_screen()
            game = Game(1, 10)
            print('-' * 30)
            game.game()
            print('-' * 30)
            input('Enter - чтобы выйти: ')
            
        elif choice_game == '1':
            clear_screen()
            game = Game(1, 100)
            print('-' * 30)
            game.game()
            print('-' * 30)
            input('Enter - чтобы выйти: ')

        elif choice_game  == '2':
            clear_screen()
            game = Game(1, 1000)
            print('-' * 30)
            game.game()
            print('-' * 30)
            input('Enter - чтобы выйти: ')

        elif choice_game == '3':
            break
        
        else:
            print(f'Ошибка! Действия "{choice_game}" не существует. Выберите существующие действие.')
            input('Enter - чтобы продолжить: ')
            continue
