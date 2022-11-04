import json
import os


class Profile:
    def __init__(self, user_file):
        self.file = user_file
        self.data = self.open_file()
        self.name = self.data['name']
        self.city = self.data['city']
        self.children = self.data['children']
        self.has = self.data['has']

    def open_file(self):
        with open(self.file, 'r') as user_file:
            return json.load(user_file)

    def get_info(self):
        print(f"The user's name is {self.name}, and he lives in {self.city}. "
              f"He has {len(self.children)} children: {', '.join(self.children)}. "
              f"He owns: {', '.join([f'{key} {value}' for key, value in self.has.items()])}.")


for file in [filename for filename in os.listdir() if filename.endswith('.json')]:
    Profile(file).get_info()
