# "Пользователя зовут John, он живет в городе New York. У него есть 2 ребенка Hanna и Peter.
# В собственности есть car Dodge, computer Apple"

import json
import os


class PersonFile:
    def __init__(self, user_name):
        self.file = user_name
        self.data = self.open_file
        self.name = self.data["name"]
        self.city = self.data["city"]
        self.children = self.data["children"]
        self.has = self.data['has']

    def open_file(self):
        with open(self.file, 'r') as user_file:
            return json.load(user_file)

    def user_info(self):
        list_info = [' '.join((key, value)) for key, value in self.has.items()]
        print(f"User's name is {self.name}, he lives in {self.city}. He has {len(self.children)} "
              f"children: {', '.join(self.children)}. He owns {', '.join(list_info)}.")


for file in [filename for filename in os.listdir() if filename.endswith('.json')]:
    PersonFile(file).user_info()
