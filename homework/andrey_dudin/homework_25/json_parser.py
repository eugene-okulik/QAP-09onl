'''
Нужно сгенерировать текст следующего вида на основе данных, имеющихся в json файлах:

"Пользователя зовут John, он живет в городе New York. У него есть 2 ребенка Hanna и Peter.
В собственности есть car Dodge, computer Apple"
'''

import json

class JsonParser:
    def __init__(self, input_file):
        self.file = input_file
        self.data = self.load_file()
        self.name = self.data['name']
        self.city = self.data['city']
        self.children = self.data['children']
        self.properties = self.data['has']

    def load_file(self):
        with open(self.file, 'r') as file:
            return json.load(file)

    def result(self):
        print(f"User name is {self.name}, he lives in {self.city}. "
              f"He has {len(self.children)} children: {', '.join(self.children)}. "
              f"He owns {', '.join([f'{k} {v}' for k, v in self.properties.items()])}.")


user1_parsing = JsonParser('user1.json')
user1_parsing.result()
user2_parsing = JsonParser('user2.json')
user2_parsing.result()
user3_parsing = JsonParser('user3.json')
user3_parsing.result()