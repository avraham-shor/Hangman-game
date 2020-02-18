import time, random
HANGMAN_ASCII_ART = """
     _    _
    | |  | |
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
    |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                         __/ |
                        |___/"""
MAX_TRIES = 7
users_points = 0

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

COLOR_END = "\033[0m"
COLOR_RED = "\033[91m"
COLOR_GREEN = "\033[92m"
COLOR_BLUE = "\033[94m"
COLOR_PINK = "\033[95m"
COLOR_TURQUOISE = "\033[94m"
COLOR_VIN = "\033[41m"

def show_logo_game_and_max_options(LOGO, MAX_TRIES):
    """Prints the welcome screen and the number of guesses
     according to the number type parameter received"""
    print("\033[45m",LOGO, MAX_TRIES,"\n",COLOR_END,"\n\n\n")

def print_hangman(num_of_tries):
    """Receives a number,
    prints the hangman according to the number received
    by randoms colors"""
    HANGMAN_PHOTOS = {
        1: STATUS_1, 2: STATUS_2, 3: STATUS_3,4: STATUS_4,
        5: STATUS_5, 6: STATUS_6, 7: STATUS_7
    }
    select_status = (HANGMAN_PHOTOS[num_of_tries])
    for i in range(len(select_status)):
        rand = random.randrange(90,99)
        print(f"\033[{rand}m",select_status[i],COLOR_END,end="")
    print()


def check_win(secret_word, old_letters_guessed):
    """The function gets two arguments,
     1) the hidden word,
      2) guess list,
     and checks whether all the characters in the word have been guessed
      than the function is multiplies the points"""
    for char in secret_word:
        if char not in old_letters_guessed:
            return False
    global users_points
    users_points *= 2
    return True


def show_hidden_word(secret_word, old_letters_guessed):
    """The function gets two arguments,
    1) the hidden word,
     2) the list of letters already guessed,
        returns the hidden word in a line of guesswork """
    return "".join([f"{char} "if char in old_letters_guessed else "_ " for char in secret_word])


def check_valid_input(letter_guessed, old_letters_guessed):
    """The function gets two arguments,
     1) Receives a guess
      2) Receives a guess list,
      returns true if the length of the letter is no more than 1 and is of the
       alphabet type and if it is not in the guess list
        otherwise it returns false """
    if letter_guessed in old_letters_guessed:
        return False
    old_letters_guessed += [letter_guessed]
    return letter_guessed.isalpha() and len(letter_guessed) == 1


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """The function gets two arguments,
     1) receives a character,
     2) receives a guess list,
     sends the guess list for testing at the "check_valid_input"
      function and if the function returns true, the character
       is added to the guess list otherwise the
       "X" character and the guess list will be printed. """
    if check_valid_input(letter_guessed, old_letters_guessed):
        return True
    else:
        print("X")
        print("".join(f"{x} -> "for x in old_letters_guessed)[:-4])
        return False


def is_rghit(letter_guessed, secret_word):
    """Receives a letter guessed and the secret word and returns true if the letter
     is already in the word and adds a point to users_points,
     if the letter is not in the word returns false and lowering a point to users_points"""
    global users_points
    right = letter_guessed in secret_word
    if right:
        users_points += 1
    else:
        if users_points > 0:
            users_points -= 1
    return right


def choose_word(file_path, index):
    """Receives two arguments,
     1) a string type parameter that contains the path to the guessing words file,
      2) receives a number to be used as an index location for guessing a word """
    file = open(file_path, "r")
    words_to_guess = file.read().split()
    return words_to_guess[(index-1) % len(words_to_guess)].lower()




def go():
    """The function is running the game"""
    num_of_tries = 1
    old_letters_guessed = []
    show_logo_game_and_max_options(HANGMAN_ASCII_ART, MAX_TRIES)
    file_path = input("Enter the path of the file of words: ")
    users_index = int(input("Enter the index of the word in file: "))
    secret_word = choose_word(file_path, users_index)
    print("Let’s start!\n\n\n")
    print(STATUS_1)
    while not check_win(secret_word, old_letters_guessed):
        print(COLOR_PINK,show_hidden_word(secret_word, old_letters_guessed),COLOR_END)
        letter_guessed = input(f"{COLOR_TURQUOISE}Enter a char to guest: {COLOR_END}").lower()
        if try_update_letter_guessed(letter_guessed ,old_letters_guessed):
            if not is_rghit(letter_guessed, secret_word):
                num_of_tries += 1
                print(":(")
                print_hangman(num_of_tries)
                if num_of_tries == 7:
                    print("LOSE")
                    time.sleep(3)
                    print(f"you succeeded to collect {users_points} points.")
                    break
    if check_win(secret_word, old_letters_guessed):
        print(COLOR_VIN, show_hidden_word(secret_word, old_letters_guessed), COLOR_END)
        time.sleep(3)
        print(COLOR_GREEN,"WIN",COLOR_END)
        print(f"you succeeded to collect {users_points} points.")


def main():
    """The main function"""
    select_user = "y"
    while select_user == "y":
        go()
        time.sleep(3)
        print("\n" * 100)
        select_user = input("Do you want to play again? (y/n) ")

if __name__ == '__main__':
    main()
