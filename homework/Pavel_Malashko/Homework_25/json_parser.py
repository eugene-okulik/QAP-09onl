import json


class UseInfo:

    def __init__(self, filename):
        self.filename = filename
        self.data = self.openfile()
        self.name = self.data['name']
        self.city = self.data['city']
        self.children = self.data['children']
        self.has = self.data['has']

    def openfile(self):
        with open(self.filename, 'r') as data_file:
            return json.load(data_file)

    def print_user_info(self):
        s = "User's name is " + self.name + ", he's living in " + self.city + " city. He has " + str(
            len(self.children)) + \
            " children: " + ', '.join(self.children) + ". He owns "
        a = list(self.has.items())
        for i in range(3):
            s += ' '.join(a[i]) + ', '
        print(s[:-2])


user1 = UseInfo('user2.json')
user1.print_user_info()

