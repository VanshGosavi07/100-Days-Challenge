# with open("./data.csv") as file:
#     x = file.readlines()
# for i in x:
#     print(i)


# import csv
#
# temperature = []
# with open("./data.csv") as file:
#     x = csv.reader(file)
#     for row in x:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
# print(temperature)


# import pandas
# data=pandas.read_csv("data.csv")
# print(data['temp'])

import pandas

# data = pandas.read_csv("data.csv")
# li = data['temp'].tolist()
# print(li)
# sum=sum(li)
# print(f"average = {sum/len(li)}")
# print(data['temp'].max())
# print(data['temp'].mean())

# data = pandas.read_csv("data.csv")
# print(data[data.condition == 'Sunny'])#for row access

data = pandas.read_csv("squirrel_data.csv")
grey = len(data[data['Primary Fur Color'] == 'Gray'])
red = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black = len(data[data['Primary Fur Color'] == 'Black'])
print(f"{grey},{red},{black}")

new_Data = {
    "Fur Color": ['grey', 'black', 'red'],
    "count": [grey, black, red]
}
df = pandas.DataFrame(new_Data)
df.to_csv('squirel_count.csv')