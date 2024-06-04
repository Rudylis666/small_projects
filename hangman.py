import sys

print("Hello in hangman game!")
lives = 10
word = "kamil"
used_letters = []
user_word=['_'] * len(word)


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

def validate_input(letter):
    if letter.isalpha() and len(letter) == 1:
        return True
    return False

def update_user_word(user_word,found_indexes,letter):
    for index in found_indexes:
        print(user_word)
        user_word[index] = letter
    return user_word

def check_game_status(user_word,lives):
    if "".join(user_word) == word:
        state_of_game()
        print("YOU WIN! ")
        return True
    if lives < 0:
        print("YOU LOST :(")
        return True
    state_of_game()

def prepare_new_game(user_word,lives,used_letters):
    user_word=['_'] * len(word)
    used_letters=[]
    lives=10
    return user_word,used_letters,lives



while True:
    while True:
        letter = input("Podaj literę: ").lower()
        if validate_input(letter):
                used_letters.append(letter)
                found_indexes = find_indexes(word, letter)
                if len(found_indexes) == 0:
                    print("Wrong letter!")
                    lives -= 1
                else:
                    update_user_word(user_word,found_indexes,letter)

                if check_game_status(user_word,lives):
                    break
        else:
            print("Only one letter please! No other characters!")
    answer = input("Do you want to play again? y/n  ")
    if answer=="n":
        break
    else:
        user_word, used_letters, lives= prepare_new_game(user_word,lives,used_letters)


# Do zrobienia:
# użytkownik nie powinien drugi raz wpisać tej samej litery, za drugim razem powinniśmy go o tym poinformować
# lista słów, zamiast jednego słowa i losować kolejne słowo do odgadnięcia
# może zewnętrzne Api do słów? pamiętanie które słowa już padły w grze
# restart gry po zakończeniu "Czy chcesz zagrać jeszcze raz"
# poziomy trudności, z inną liczzbą żyć
