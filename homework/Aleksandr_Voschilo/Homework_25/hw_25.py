import json


class PersonFile:
    def __init__(self, file):
        self.file = file
        self.data = self.open_file()
        self.name = self.data['name']
        self.city = self.data['city']
        self.children = self.data['children']
        self.has = self.data['has']

    def open_file(self):
        with open(self.file, 'r') as user_file:
            return json.load(user_file)

    def user_info(self):
        print(f"The user's name is {self.name}, and he lives in {self.city}. "
              f"He has {len(self.children)} children: {', '.join(self.children)}. "
              f"He owns: {', '.join([f'{k} {v}' for k, v in self.has.items()])}.")


user_1 = PersonFile('user1.json')
user_1.user_info()

user_2 = PersonFile('user2.json')
user_2.user_info()

user_3 = PersonFile('user3.json')
user_3.user_info()
