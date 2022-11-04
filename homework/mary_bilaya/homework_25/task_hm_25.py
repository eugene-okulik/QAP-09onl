import json


class PersonalData:
    def __init__(self, user_file):
        self.user_file = user_file
        self.user_data = self.read_json_file()    # user_data - contains the contents of the data_file
        self.name = self.user_data['name']
        self.city = self.user_data['city']
        self.children = self.user_data['children']
        self.has = self.user_data['has']

    def read_json_file(self):
        with open(self.user_file, 'r') as data_file:
            return json.load(data_file)

    def user_info(self):
        print(f'The users name is {self.name}. '
              f'He has lived in {self.city}. '
              f'He has {len(self.children)} children. Their names are {", ".join(self.children)}. '
              f'He owns: ')
        for key, value in self.has.items():
            print(f'{key}{value}', end=", ")


user_1 = PersonalData('user1.json')
print(user_1.user_info())
print('\n')
user_2 = PersonalData('user2.json')
print(user_2.user_info())
print('\n')
user_3 = PersonalData('user3.json')
print(user_3.user_info())


