import json


class Person:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.open_file()
        self.name = self.data['name']
        self.city = self.data['city']
        self.children = self.data['children']
        self.has = self.data['has']

    def open_file(self):
        with open(self.filename, 'r') as data_file:
            return json.load(data_file)

    def display(self):
        print(f"Пользователя зовут {self.name}, он живет в городе {self.city}."
              f" У него есть {len(self.children)} ребенка: {', '.join(self.children)}. "
              f"В собственности есть {', '.join([f'{key} {value}' for key, value in self.has.items()])}.")


data1 = Person('user1.json')
data1.display()

data2 = Person('user2.json')
data2.display()

data3 = Person('user3.json')
data3.display()
