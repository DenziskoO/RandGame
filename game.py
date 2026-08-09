import random
from pathlib import Path
import json

class Game():
    def __init__(self, min_num, max_num):
        self.count = 0
        self.min_num = min_num
        self.max_num = max_num
        self.number = random.randint(self.min_num, self.max_num)

    def check_record(self):
        path = Path('record.json')
        try: 
            contents = path.read_text()
            record = json.loads(contents)
        except FileNotFoundError:
            record = 0
        if record == 0:
            contents = json.dumps(self.count)
            path.write_text(contents)
        elif self.count < record:
            contents = json.dumps(self.count)
            path.write_text(contents)    

    def game(self):
        print(f'Я загадал число от {self.min_num} до {self.max_num}. Попробуй отгадать его ниже:')

        while True:
            try:
                choice = int(input('\nВведи свою догадку: '))
                self.count += 1

                if choice < self.number:
                    print('Неверно! Мое число больше, попробуй еще раз.')
                elif choice > self.number:
                    print('Неверно! Мое число меньше, попробуй еще раз.')
                else:
                    self.check_record()
                    print(f'Верно! Всего сделано попыток: {self.count}')
                    break
            except ValueError:
                print(f'Невернo! Пожалуйста, вводите только числа!')
                continue
