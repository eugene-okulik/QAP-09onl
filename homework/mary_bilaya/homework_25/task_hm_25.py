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

    def name_info(self):
        return f'The users name is {self.name}. '

    def city_info(self):
        return f'He has lived in {self.city}. '

    def children_info(self):
        return f'He has {len(self.children)} children. Their names are {", ".join(self.children)}.'

    def has_info(self):
        print('He owns: ', end="")
        for key, value in self.has.items():
            print(f'{key} {value}', end=", ")


user_1 = PersonalData('user1.json')
print(user_1.name_info())
print(user_1.city_info())
print(user_1.children_info())
print(user_1.has_info())
print('\n')
user_2 = PersonalData('user2.json')
print(user_2.name_info())
print(user_2.city_info())
print(user_2.children_info())
print(user_2.has_info())
print('\n')
user_3 = PersonalData('user3.json')
print(user_3.name_info())
print(user_3.city_info())
print(user_3.children_info())
print(user_3.has_info())

