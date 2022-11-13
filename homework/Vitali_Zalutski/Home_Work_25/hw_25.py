import json


class Users:
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

    def user_info(self):
        own = None
        own_1 = []
        own_2 = []
        for key, value in self.has.items():
            own_1.append(key)
            own_2.append(value)
            own = [': '.join(x) for x in zip(own_1, own_2)]

        print(f'He name is {self.name}, he lives in the {self.city} city. He has {len(self.children)} children: '
              f"{', '.join(self.children)}. The property has {', '.join(own)}")


user_1 = Users('user1.json')
user_1.user_info()
user_2 = Users('user2.json')
user_2.user_info()
user_3 = Users('user3.json')
user_3.user_info()
