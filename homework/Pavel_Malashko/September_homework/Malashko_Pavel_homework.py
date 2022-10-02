class Files:
    def __init__(self):
        self.list = []

    def add_to_files(self, files):
        for file in files:
            self.list.append(file)


class Statistic:
    @staticmethod
    def get_statistic(files):
        general_sum_digits = 0  # Переменная для хранения суммы чисел во всех файлов
        unique_letters = {}  # Словарь для хранения уникальных букв и их количества
        sum_punctuation_marks = 0  # Общее количество знаков препинания
        sum_other_symbols = 0  # Общее количество спецсимволов, не включая знаки препинания
        for file in files:  # Перебираем файлы из списка
            with open(file) as file_for_statistic:
                digit_count = 0
                letter_count = 0
                other_symbols = 0
                punct_marks = 0
                sum_digit = 0
                punctuation_marks = ['!', '-', '(', ')', ',', '.', ':', ';', '?']
                max_count_array = {}  # Словарь для хранения букв и их количества в файле
                s = file_for_statistic.read().lower()  # Чтение файла и приведения к нижнему регистру всех букв(для
                # удобного подсчета в будущем)
                for symbol in s:
                    if symbol.isdigit():
                        digit_count += 1
                        sum_digit += int(symbol)
                    elif symbol.isalpha():
                        letter_count += 1
                        max_count_array[symbol] = s.count(symbol)  # Заносим в словарь букву и количество этих букв в
                        # файле
                    elif symbol in punctuation_marks:
                        punct_marks += 1
                    else:
                        other_symbols += 1

            unique_letters[file] = len(max_count_array.keys())  # Заносим в словарь файл и количество уникальных букв
            # в файле
            general_sum_digits += sum_digit
            sum_punctuation_marks += punct_marks
            sum_other_symbols += other_symbols
            b = sorted(max_count_array.items(), key=lambda item: -item[1])  # Сортируем по убыванию словарь с буквами и
            # их количеством по значению
            print(f"Файл: {file_for_statistic.name}")
            print(f"{letter_count} букв, {digit_count} цифр, {punct_marks + other_symbols} символов")
            print(f"Среднее арифметическое: {sum_digit / digit_count}")
            print("Топ 3 букв:")
            print(f"{b[0][0].upper()} - количество: {b[0][1]}")
            print(f"{b[1][0].upper()} - количество: {b[1][1]}")
            print(f"{b[2][0].upper()} - количество: {b[2][1]}")
            print()

        for i in range(len(files)):  # Вывод файла в котором больше всего уникальных букв, и если количество одинаковое
            if set(unique_letters.items()) == 1:
                print("Количество уникальных чисел одинаково")
                break
            else:
                m = sorted(unique_letters.items(), key=lambda item: -item[1])
                print(f"В файле {m[0][0]} больше всего уникальных букв {m[0][1]}")
                break
        print(f"Сумма всех чисел: {general_sum_digits}")
        print(f"Всего в файлах {sum_punctuation_marks} знаков препинания и {sum_other_symbols} прочих спецсимволов")


files_array = ['file7.txt', 'file8.txt', 'file9.txt']

our_files = Files()
our_files.add_to_files(files_array)

statistic1 = Statistic()
statistic1.get_statistic(our_files.list)
