# numbers=[1,2,3]
# new=[n+1 for n in numbers]
# print(new)

# numbers = [1, 2, 3]
# new = [numbers[i] + 1 for i in range(0, len(numbers))]
# print(new)

# names = ['vansh', 'harsha', 'disha']
# new = [name for name in names if len(name) < 6]
# print(new)

# names = ['vansh', 'harsha', 'disha']
# new = [name.upper() for name in names if len(name) < 6]
# print(new)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# new = [number*number for number in numbers]
# print(new)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# new = [number for number in numbers if number % 2 == 0]
# print(new)

import random

# name = ['vansh', 'harsh', 'divya', 'ram', 'surya']
# new_dict = {names: random.randint(0, 100) for names in name}
# print(new_dict)
#
# passed_stud = {key: value for (key, value) in new_dict.items() if value >= 60}
# print(passed_stud)


# sentence = 'What is the Airspeed Velocity of an Unladen Swallow'
# li = sentence.split()
# new_dict = {key: len(key) for key in li}
# print(new_dict)
#
#
# weather = {
#     'Monday': 12,
#     'Tuesday': 14,
#     'Wednesday': 15,
#     'Thursday': 14,
#     'Friday': 21,
#     'Saturday': 22,
#     'Sunday': 24,
# }
#
# dict = {key: ((value * 9) / 5) + 32 for (key, value) in weather.items()}
# print(dict)


import pandas

file = pandas.read_csv("data.csv")
data = pandas.DataFrame(file)
name = input("Enter name :\n").upper()
li = []
for item in name:
    li.append(item)

dictionary = {row.letter: row.code for (index, row) in data.iterrows()}
new = [dictionary[item] for item in li]
print(new)
