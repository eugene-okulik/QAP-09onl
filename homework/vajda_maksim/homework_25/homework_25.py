import json

"""В этой папке находится 3 json файла.
Нужно сгенерировать текст следующего вида на основе данных, имеющихся в json файлах:

    "Пользователя зовут John, он живет в городе New York. У него есть 2 ребенка Hanna и Peter. 
    В собственности есть car Dodge, computer Apple"

Это пример для файла user1.json. 
Важно, чтобы в результате получился один код, который умеет генерировать этот текст из любого из этих трех файлов.
Папка с файлами залита в ветку main. 
Для удобства можете скопировать (не переместить!) эти файлы к себе в папку с выполнением задания.
Для красоты, можете сгенерировать этот текст на английском.
"""


class JsonHM:

    def __init__(self, file_name):
        self.file_name = file_name
        self.user = self.open_file()
        self.name = self.user['name']
        self.city = self.user['city']
        self.children = self.user['children']
        self.has = self.user['has']

    def open_file(self):
        with open(self.file_name, 'r') as data_file:
            return json.load(data_file)

    def text_generation(self):
        children = ' and '.join(self.children)
        has = ', '.join([f'{k} {v}' for k, v in self.has.items()])
        print(f'The user’s name is {self.name}, he lives in {self.city}. '
              f'He has {len(self.children)} children {children}. '
              f'His property are: {has}')


user1 = JsonHM('user1.json')
user2 = JsonHM('user2.json')
user3 = JsonHM('user3.json')
user1.text_generation()
user2.text_generation()
user3.text_generation()
