import random

print("Hello in hangman game!")
lives = 10
words = ["kot", "pies", "koala"]
los = random.randrange(0, len(words))
word = words[los]
del words[los]

used_letters = []
user_word = ['_'] * len(word)


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

def validate_input(letter,used_letters):
    if letter in used_letters:
        print("This letter is already used, enter another ;)")
        return False
    if letter.isalpha() and len(letter) == 1:
        return True
    else:
        print("Only one letter please! No other characters!")
    return False

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
    if lives < 0:
        print("YOU LOST :(")
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
    if answer == "n":
        return False
    else:
        return True

while True:
    while True:
        letter = input("Podaj literę: ").lower()
        if validate_input(letter,used_letters):
            used_letters.append(letter)
            found_indexes = find_indexes(word, letter)
            if len(found_indexes) == 0:
                print("Wrong letter!")
                lives -= 1
            else:
                update_user_word(user_word, found_indexes, letter)

            if check_game_status(user_word, lives):
                break

    if len(words) > 0:
        if not another_game():
            break
        else:
            user_word, lives, used_letters, word = prepare_new_game()
    else:
        break

# Do zrobienia:
# użytkownik nie powinien drugi raz wpisać tej samej litery, za drugim razem powinniśmy go o tym poinformować
# może zewnętrzne Api do słów? pamiętanie które słowa już padły w grze
# poziomy trudności, z inną liczzbą żyć
