import random


def users_words():
    words = []
    choice = input("Do you want to create your own list of words? y/n ")
    if choice.isalpha() and len(choice) == 1:
        if choice == 'y':
            number_of_words = int(input("How many words do you want to put in game? "))
            for i in range(0, number_of_words):
                new_word = input("Enter your word: ")
                if new_word.isalpha():
                    words.append(new_word)

        elif choice == 'n':
            words = my_words
        else:
            print("Choose between y and n")
            users_words()
    else:
        print("Choose between y and n")
        users_words()

    return words


print("Hello in hangman game!")
lives = 8
my_words = ["kot", "pies", "koala"]
words = users_words()
los = random.randrange(0, len(words))
word = words[los]
del words[los]
used_letters = []
user_word = ['_'] * len(word)
PICTURES = (
    """
    ----------
    |    |
    |    
    |
    |
    |
    |
    |
    |
    |
    ----------
    """,
    """
    ----------
    |    |
    |    O
    |
    |
    |
    |
    |
    |
    |
    ----------
    """,
    """
    ----------
    |    |
    |    O
    |   -+-
    |
    |
    |
    |
    |
    |
    ----------
    """,
    """
    ----------
    |    |
    |    O
    |   -+-
    |  /
    | /
    |
    |
    |
    |
    ----------
    """,
    """
    ----------
    |    |
    |    O
    |   -+-
    |  /    \\
    | /      \\
    |
    |
    |
    |
    ----------
    """,
    """
    ----------
    |    |
    |    O
    |   -+-
    |  / |  \\
    | /  |   \\
    |    |
    |
    |
    |
    ----------
    """,
    """
    ----------
    |    |
    |    O
    |   -+-
    |  / |  \\
    | /  |   \\
    |    |
    |   |
    |   |
    |   |
    ----------
    """,
    """
    ----------
    |    |
    |    O
    |   -+-
    |  / |  \\
    | /  |   \\
    |    |
    |   |  |
    |   |  |
    |   |  |
    ----------
    """
)


def find_indexes(word, letter):
    indexes = []
    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)

    return indexes


def state_of_game():
    print()
    print(user_word)
    print("Number of lives: ", lives)
    print("Used letters: ", used_letters)
    print()


def validate_input(letter, used_letters):
    if letter in used_letters:
        print("This letter is already used, enter another ;)")
        return False
    if letter.isalpha() and len(letter) == 1:
        return True
    else:
        print("Only one letter please! No other characters!")


def update_user_word(user_word, found_indexes, letter):
    for index in found_indexes:
        print(user_word)
        user_word[index] = letter
    return user_word


def check_game_status(user_word, lives):
    if "".join(user_word) == word:
        state_of_game()
        print("YOU WIN! ")
        return True
    if lives <= 0:
        print("YOU LOST :(")
        print(PICTURES[7])
        return True
    state_of_game()


def prepare_new_game():
    used_letters = []
    lives = 10
    los = random.randrange(0, len(words))
    word = words[los]
    del words[los]
    user_word = ['_'] * len(word)
    return user_word, lives, used_letters, word


def another_game():
    answer = input("Do you want to play again? y/n  ")
    if answer.isalpha() and len(answer) == 1:
        if answer == "y":
            return True
        else:
            return False
    elif len(answer) != 1:
        print("Enter one letter please")
        another_game()


while True:
    while True:
        letter = input("Podaj literę: ").lower()
        if validate_input(letter, used_letters):
            used_letters.append(letter)
            found_indexes = find_indexes(word, letter)
            if len(found_indexes) == 0:
                print("Wrong letter!")
                print(PICTURES[8 - lives])
                lives -= 1
            else:
                update_user_word(user_word, found_indexes, letter)

            if check_game_status(user_word, lives):
                break

    if len(words) > 0:
        if not another_game():
            print("See you soon!")
            break
        else:
            user_word, lives, used_letters, word = prepare_new_game()
    else:
        break

# Do zrobienia:
# wprowadzanie swoich słów
