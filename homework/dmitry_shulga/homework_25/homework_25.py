import json


class Represent:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.open_file()
        self.name = self.data["name"]
        self.city = self.data["city"]
        self.children = self.data["children"]
        self.has = self.data['has']

    def open_file(self):
        with open(self.filename, "r") as f:
            return json.load(f)

    def formatted_text(self):
        my_own = None
        m_own = []
        y_own = []
        for key, value in self.has.items():
            m_own.append(key)
            y_own.append(value)
            my_own = [': '.join(x) for x in zip(m_own, y_own)]

        print(f"User name {self.name}, he lives in the city {self.city}. He has {len(self.children)} children: "
              f"{', '.join(self.children)}. The property has {', '.join(my_own)}")


data_1 = Represent("user1.json")
data_1.formatted_text()
data_2 = Represent("user2.json")
data_2.formatted_text()
data_3 = Represent("user3.json")
data_3.formatted_text()

