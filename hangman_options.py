num_of_tries = 6


STATUS_1 = """
x-------x"""

STATUS_2 = """
x-------x
        |
        |
        |
        |
        |"""

STATUS_3 = """
x-------x
|       |
|       0
|
|
|"""

STATUS_4 = """
x-------x
|       |
|       0
|
|
|"""
STATUS_5 = """
x-------x
|       |
|       0
|      /|\\
|
|"""

STATUS_6 = """
x-------x
|       |
|       0
|      /|\\
|      /
|"""


STATUS_7 = """ 
x-------x
|       |
|       0
|      /|\\
|      / \\
|
"""



def print_hangman(num_of_tries):
    HANGMAN_PHOTOS = {1: STATUS_1, 2: STATUS_2, 3: STATUS_3, 4: STATUS_4, 5: STATUS_5, 6: STATUS_6, 7: STATUS_7}
    return (HANGMAN_PHOTOS[num_of_tries])



def main():
    print_hangman(5)


if __name__ == '__main__':
    main()









#
#
# print("""  _    _
#  | |  | |
#  | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
#  |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
#  | |  | | (_| | | | | (_| | | | | | | (_| | | | |
#  |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
#                       __/ |
#                      |___/""")
#
# print("""picture 1:
#     x-------x
#
# picture 2:
#     x-------x
#     |
#     |
#     |
#     |
#     |
#
# picture 3:
#     x-------x
#     |       |
#     |       0
#     |
#     |
#     |
#
# picture 4:
#     x-------x
#     |       |
#     |       0
#     |       |
#     |
#     |
#
# picture 5:
#     x-------x
#     |       |
#     |       0
#     |      /|\\
#     |
#     |
#
# picture 6:
#     x-------x
#     |       |
#     |       0
#     |      /|\\
#     |      /
#     |
#
# picture 7:
#     x-------x
#     |       |
#     |       0
#     |      /|\\
#     |      / \\
#     |""")