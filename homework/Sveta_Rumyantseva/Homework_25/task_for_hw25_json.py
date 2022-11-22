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
        with open(self.filename, 'r') as file:
            return json.load(file)

    def obtain_user_info(self):
        has_list = [' '.join((key, value)) for key, value in self.has.items()]
        print(f"User's name is {self.name}, he lives in {self.city}. He has {len(self.children)} "
              f"children: {', '.join(self.children)}. He owns {', '.join(has_list)}.")


# "Пользователя зовут John, он живет в городе New York. У него есть 2 ребенка Hanna и Peter.
# В собственности есть car Dodge, computer Apple"
for i in range(1, 4):
    data = Person(f"user{i}.json")
    data.obtain_user_info()
