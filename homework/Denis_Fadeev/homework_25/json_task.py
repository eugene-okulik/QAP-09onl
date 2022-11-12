import json


class UserInformation:
    def __init__(self, file):
        self.file = file
        self.data = self.open_file()
        self.name = self.data['name']
        self.city = self.data['city']
        self.children = self.data['children']
        self.has = self.data['has']

    def open_file(self):
        with open(self.file, 'r') as data:
            return json.load(data)

    def input_information_users(self):
        print(f'User name is {self.name}, he lives in {self.city}. '
              f'He has {len(self.children)} children: {", ".join(self.children)}. '
              f'He owns: ')
        for key, value in self.has.items():
            print(', '.join([f'{key}-{value}']), end='')


user_1 = UserInformation('user1.json')
user_1.input_information_users()
print('\n')
user_2 = UserInformation('user2.json')
user_2.input_information_users()
print('\n')
user_3 = UserInformation('user3.json')
user_3.input_information_users()
print('\n')
