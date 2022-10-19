import os


class TextFile:
    def __init__(self, file_name):
        self.file_name = file_name
        self.digits_list = []
        self.unique_letters = set()
        self.punctuation = []
        self.spec_symbols = []
        self.file_content = self.open_file()
        self.letters_count, self.digits_count, self.symbols_count = self.count_types()
        self.avg = sum(self.digits_list) / len(self.digits_list)
        self.top_3 = self.build_top_3()
        self.digits_sum = sum(self.digits_list)

    def open_file(self):
        with open(self.file_name, 'r') as text_file:
            return text_file.read()

    def count_types(self):
        alfas = digits = symbols = 0
        for char in self.file_content:
            if char.isalpha():
                alfas += 1
                self.unique_letters.add(char.lower())
            elif char.isdigit():
                digits += 1
                self.digits_list.append(int(char))
            else:
                symbols += 1
                if char in ['!', '-', '(', '),', ',', '.', ':', ';', '?']:
                    self.punctuation.append(char)
                else:
                    self.spec_symbols.append(char)
        return alfas, digits, symbols

    def build_top_3(self):
        unique_dict = {letter: self.file_content.lower().count(letter) for letter in self.unique_letters}
        sorted_unique_dict = dict(sorted(unique_dict.items(), key=lambda x: x[1], reverse=True))
        iter_unique_dict = iter(sorted_unique_dict.items())
        top_3 = {}
        while len(top_3) < 3:
            letter, count = next(iter_unique_dict)
            top_3[letter] = count
        return top_3




files = [filename for filename in os.listdir() if filename.endswith('.txt')]
unique_counts = set()
unique_result = (None, 0)
sum_digits_result = 0
all_punctuation = []
all_spec_symbols = []
for file_name in files:
    file_data = TextFile(file_name)
    file_result = f'''{file_name}
{file_data.letters_count} букв, {file_data.digits_count} цифр, {file_data.symbols_count} символов
среднее арифметическое: {file_data.avg}
Топ 3 букв:
'''
    for letter, count in file_data.top_3.items():
        file_result += f'{letter.upper()} - количество: {count}\n'

    print(file_result)

    if len(file_data.unique_letters) > unique_result[1]:
        unique_result = (file_name, len(file_data.unique_letters))
    unique_counts.add(len(file_data.unique_letters))
    sum_digits_result += file_data.digits_sum
    all_punctuation.extend(file_data.punctuation)
    all_spec_symbols.extend(file_data.spec_symbols)

if len(unique_counts) > 1:
    print(f'В файле {unique_result[0]} больше всего уникальных букв ({unique_result[1]})')
else:
    print('Во всех вайлах одинаковое количество уникальных букв')
print(f'Сумма всех чисел: {sum_digits_result}')
print(f'Всего в файлах {len(all_punctuation)} знаков препинания и {len(all_spec_symbols)} прочих спецсимволов')

