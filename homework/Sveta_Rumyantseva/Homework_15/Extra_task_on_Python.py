import operator


class TextFile:
    def __init__(self, name):
        self.name = name

    def read_file(self):
        with open(self.name) as f:
            i = 0
            symbols = f.read()
            eng_letters_list, numbers_list, spec_chars_list, punctuation_list = [], [], [], []
            while i < len(symbols):
                if symbols[i].isalpha():
                    eng_letters_list.append(symbols[i])
                elif symbols[i].isdigit():
                    numbers_list.append(int(symbols[i]))
                elif symbols[i] in "!-()\",.:;?'":
                    punctuation_list.append(symbols[i])
                    spec_chars_list.append(symbols[i])
                else:
                    spec_chars_list.append(symbols[i])
                i += 1
        """from file7 or file8 or file9 to create "eng_letters_list" - the list of only english letters, 
        "numbers_list"-the list of only numbers, "punctuation_list"- the list of only punctuation symbols, 
        "spec_chars_list"- the list of the special symbols"""
        return eng_letters_list, numbers_list, spec_chars_list, punctuation_list

    @staticmethod
    def count_letters(eng_letters_list):
        letters_counter = len(eng_letters_list)  # the number of the english letters in a file
        return letters_counter

    @staticmethod
    def count_digits(numbers_list):
        digits_counter = len(numbers_list)  # the number of the numbers in a file
        return digits_counter

    @staticmethod
    def count_spec_chars(spec_chars_list):
        spec_chars_counter = len(spec_chars_list)  # the number of all special symbols in a file
        return spec_chars_counter

    @staticmethod
    def count_arithmetic_average(numbers_list):
        return sum(numbers_list) / len(numbers_list)  # calculate the arithmetic_average of all numbers in a file

    @staticmethod
    def count_3leader_letters(eng_letters_list):
        english_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        eng_letters_str = "".join(eng_letters_list).upper()
        my_dict = {elem: eng_letters_str.count(elem) for elem in english_alphabet}
        # descending sort by values of my_dict and getting sorted_dict - the list of the tuples (key, value)
        sorted_dict = sorted(my_dict.items(), key=operator.itemgetter(1), reverse=True)
        return sorted_dict

    @staticmethod
    def count_unique_letters(eng_letters_list):
        english_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        counter = 0
        eng_letters_str = "".join(eng_letters_list).upper()
        for elem in english_alphabet:
            if eng_letters_str.count(elem) == 1:
                counter += 1
                # print(elem)
        return counter  # the number of the unique english letters without case in a file

    @staticmethod
    def count_sum_digits(numbers_list):
        return sum(numbers_list)  # the amount of the numbers in a file

    @staticmethod
    def count_punctuation(punctuation_list, spec_chars_list):
        # the number of the punctuation symbols and other special symbols in a file
        return len(punctuation_list), len(spec_chars_list) - len(punctuation_list)


f7 = TextFile("file7.txt")
result_reading7 = f7.read_file()
print(f"The number of the english letters are {f7.count_letters(result_reading7[0])} in file7")
print(f"The number of the digits are {f7.count_digits(result_reading7[1])} in file7")
print(f"The number of the specific chars are {f7.count_spec_chars(result_reading7[2])} in file7")
print(f"The arithmetic average of all digits is {f7.count_arithmetic_average(result_reading7[1])} in file7")
print(f"The first leader of all the letters is {f7.count_3leader_letters(result_reading7[0])[0][0]} = "
      f"{f7.count_3leader_letters(result_reading7[0])[0][1]} in file7")
print(f"The second leader of all the letters is {f7.count_3leader_letters(result_reading7[0])[1][0]} = "
      f"{f7.count_3leader_letters(result_reading7[0])[1][1]} in file7")
print(f"The third leader of all the letters is {f7.count_3leader_letters(result_reading7[0])[2][0]} = "
      f"{f7.count_3leader_letters(result_reading7[0])[2][1]} in file7")
unique_letters_f7 = f7.count_unique_letters(result_reading7[0])
print(f"The number of the unique_letters are {unique_letters_f7} in file7")

# compare The number of the unique_letters from each file
punctuation_symbols_f7 = f7.count_punctuation(result_reading7[3], result_reading7[2])[0]
spec_symbols_f7 = f7.count_punctuation(result_reading7[3], result_reading7[2])[1]
print(f"The number of the punctuation symbols are {punctuation_symbols_f7} "
      f"and other specific symbols are {spec_symbols_f7} in file7")
print("----------------------------")

f8 = TextFile("file8.txt")
result_reading8 = f8.read_file()
print(f"The number of the english letters are {f8.count_letters(result_reading8[0])} in file8")
print(f"The number of the digits are {f8.count_digits(result_reading8[1])} in file8")
print(f"The number of the specific chars are {f8.count_spec_chars(result_reading8[2])} in file8") 
print(f"The arithmetic average of all digits is {f8.count_arithmetic_average(result_reading8[1])} in file8")
print(f"The first leader of all the letters is {f8.count_3leader_letters(result_reading8[0])[0][0]} = "
      f"{f8.count_3leader_letters(result_reading8[0])[0][1]} in file8")
print(f"The second leader of all the letters is {f8.count_3leader_letters(result_reading8[0])[1][0]} = "
      f"{f8.count_3leader_letters(result_reading8[0])[1][1]} in file8")
print(f"The third leader of all the letters is {f8.count_3leader_letters(result_reading8[0])[2][0]} = "
      f"{f8.count_3leader_letters(result_reading8[0])[2][1]} in file8")
unique_letters_f8 = f8.count_unique_letters(result_reading8[0])
print(f"The number of the unique_letters are {unique_letters_f8} in file8")
punctuation_symbols_f8 = f8.count_punctuation(result_reading8[3], result_reading8[2])[0]
spec_symbols_f8 = f8.count_punctuation(result_reading8[3], result_reading8[2])[1]
print(f"The number of the punctuation symbols are {punctuation_symbols_f8} "
      f"and other specific symbols are {spec_symbols_f8} in file8")
print("----------------------------")

f9 = TextFile("file9.txt")
result_reading9 = f9.read_file()
print(f"The number of the english letters are {f9.count_letters(result_reading9[0])} in file9")
print(f"The number of the digits are {f9.count_digits(result_reading9[1])} in file9")
print(f"The number of the specific chars are {f9.count_spec_chars(result_reading9[2])} in file9")
print(f"The arithmetic average of all digits is {f9.count_arithmetic_average(result_reading9[1])} in file9")
print(f"The first leader of all the letters is {f9.count_3leader_letters(result_reading9[0])[0][0]} = "
      f"{f9.count_3leader_letters(result_reading9[0])[0][1]} in file9")
print(f"The second leader of all the letters is {f9.count_3leader_letters(result_reading9[0])[1][0]} = "
      f"{f9.count_3leader_letters(result_reading9[0])[1][1]} in file9")
print(f"The third leader of all the letters is {f9.count_3leader_letters(result_reading9[0])[2][0]} = "
      f"{f9.count_3leader_letters(result_reading9[0])[2][1]} in file9")
unique_letters_f9 = f9.count_unique_letters(result_reading9[0])
print(f"The number of the unique_letters are {unique_letters_f9} in file9")
# compare The number of the unique_letters from each file
punctuation_symbols_f9 = f9.count_punctuation(result_reading9[3], result_reading9[2])[0]
spec_symbols_f9 = f9.count_punctuation(result_reading9[3], result_reading9[2])[1]
print(f"The number of the punctuation symbols are {punctuation_symbols_f9} "
      f"and other specific symbols are {spec_symbols_f9} in file9")
print("----------------------------")


if unique_letters_f7 < unique_letters_f9 and unique_letters_f8 < unique_letters_f9:
    print(f"There are more unique letters in file 9 than in other files: {f9.count_unique_letters(result_reading9[0])}")
elif unique_letters_f7 < unique_letters_f8 and unique_letters_f9 < unique_letters_f8:
    print(f"There are more unique letters in file 8 than in other files: {f8.count_unique_letters(result_reading8[0])}")
elif unique_letters_f8 < unique_letters_f7 and unique_letters_f9 < unique_letters_f7:
    print(f"There are more unique letters in file 7 than in other files: {f7.count_unique_letters(result_reading7[0])}")
elif unique_letters_f7 == unique_letters_f8 == unique_letters_f9:
    print(f"There are the same number of the unique letters in three files: "
          f"{f8.count_unique_letters(result_reading8[0])}")
elif unique_letters_f7 == unique_letters_f8:
    print(f"There are the same number of the unique letters in file 7 and file 8: "
          f"{f7.count_unique_letters(result_reading7[0])}")
elif unique_letters_f7 == unique_letters_f9:
    print(f"There are the same number of the unique letters in file 7 and file 9: "
          f"{f7.count_unique_letters(result_reading7[0])}")
else:
    print(f"There are the same number of the unique letters in file 8 and file 9: "
          f"{f8.count_unique_letters(result_reading8[0])}")


sum_result = (f7.count_sum_digits(result_reading7[1]) + f8.count_sum_digits(result_reading8[1]) +
              f9.count_sum_digits(result_reading9[1]))
print(f"The total amount of the all digits out of three files is {sum_result}.")

print(f"There are the punctuation symbols in three files: "
      f"{punctuation_symbols_f7 + punctuation_symbols_f8 + punctuation_symbols_f9} "
      f"and other specific symbols in three files: {spec_symbols_f7 + spec_symbols_f8 + spec_symbols_f9}")
