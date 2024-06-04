import sys

print("Hello in hangman game!")
lives = 10
word = "kamil"
user_word = []
used_letters = []


def find_indexes(word, letter):
    indexes = []
    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)

    return indexes

def state_of_game():
    print()
    print(user_word)
    print("Number of lives: ",lives)
    print("Used letters: ",used_letters)
    print()


for _ in word:
    user_word.append("_")

while True:
    letter = input("Podaj literę: ").lower()
    if letter.isalpha():
        if len(letter)==1:
            used_letters.append(letter)
            found_indexes = find_indexes(word, letter)
            if len(found_indexes) == 0:
                print("Wrong letter!")
                lives -= 1

            else:
                for index in found_indexes:
                    user_word[index] = letter

                if "".join(user_word) == word:
                    print("YOU WIN! ")
                    sys.exit(0)

            if lives < 0:
                print("YOU LOST :(")
                sys.exit(0) #kończenie programu bez żadnego błędu
            state_of_game()
        else:
            print("Only one letter please...")
    else:
        print("Only letters...")

#Do zrobienia:
# Walidacja wprowadzonych danych, cyfr, znaków specjalnych, etc, zamiana liter na małe też by się przydała
# walidacja czy użytkownik wprowadził tylko jedną literę
# użytkownik nie powinien drugi raz wpisać tej samej litery, za drugim razem powinniśmy go o tym poinformować
# lista słów, zamiast jednego słowa i losować kolejne słowo do odgadnięcia
# może zewnętrzne Api do słów? pamiętanie które słowa już padły w grze
# restart gry po zakończeniu "Czy chcesz zagrać jeszcze raz"
# poziomy trudności, z inną liczzbą żyć