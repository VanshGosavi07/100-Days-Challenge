# try:
#     open('abc.txt', 'r')
#     print(dict['unknownkkey'])
# except FileNotFoundError:
#     print('file is not exits')
# else:
#     print('its else block')
# finally:
#     print("finally")

# fruits = ['Apple', 'Pear', 'Orange']
#
#
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print('list index out of range')
#     else:
#         print(fruit + " pie")
#
#
# make_pie(2)

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3},
]
total_likes = 0
for post in facebook_posts:
    try:
        likes = post['Likes']
    except KeyError:
        pass
    else:
        total_likes += likes
print(total_likes)
