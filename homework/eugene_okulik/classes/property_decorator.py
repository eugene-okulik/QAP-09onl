import json


class CountryFile:
    favorite = None

    def __init__(self, filename):
        self.__filename = filename
        self.__data = self.open_file()
        self.__country = self.__data['country']
        self.__avg_temp = self.__data['avg_temp']

    @property
    def avg_temp(self):
        return self.__avg_temp

    @avg_temp.setter
    def avg_temp(self, value):
        self.__avg_temp = value

    def open_file(self):
        with open(self.__filename, 'r') as data_file:
            return json.load(data_file)  # Returns dict


data1 = CountryFile('data1.txt')
data1.favorite = True
data1.avg_temp = 45
print(data1.favorite)
print(data1.avg_temp)
