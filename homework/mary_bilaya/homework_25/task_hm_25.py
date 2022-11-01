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
        owns = list(self.has.items())











user_1 = PersonalData('user1.json')
print(user_1.name_info())
print(user_1.city_info())
print(user_1.children_info())
print(user_1.has_info())

