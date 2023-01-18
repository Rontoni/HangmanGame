"""
Hangman Game
"""

from random import choice

# Words for the game
words = ['motivation', 'appointment', 'discovery', 'caligraphy', 'rendering']
correct_letters = []
incorrect_letters = []
tries = 6
right_answers = 0
game_over = False

# Function for picking a word


def choose_word(list_of_words):
    chosen_word = choice(list_of_words)
    different_letters = len(set(chosen_word))

    return chosen_word, different_letters


# Function for picking a letter


def ask_letter():
    chosen_letter = ''
    is_valid = False
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    while not is_valid:
        chosen_letter = input("Please choose a letter:")

        if chosen_letter in alphabet and len(chosen_letter) == 1:
            is_valid = True
        else:
            print("You haven't chosen a correct letter")

    return chosen_letter

# Function for showing the board while picking words


def show_new_board(chosen_word):
    hidden_list = []

    for c in chosen_word:
        if c in correct_letters:
            hidden_list.append(c)
        else:
            hidden_list.append('-')
    print(' '.join(hidden_list))

# Function for checking if the letter entered and matching words.
# Also attempts left.


def check_letter(chosen_letter, hidden_word, tries, matches):
    end = False

    if chosen_letter in hidden_word:
        correct_letters.append(chosen_letter)
        matches += 1
    else:
        incorrect_letters.append(chosen_letter)
        tries -= 1

    if tries == 0:
        end = lose()
    elif matches == unique_letters:
        end = win(hidden_word)

    return tries, end, matches

# Function for loosing the game


def lose():
    print("You don't have any tries left")
    print("The hidden word was " + word)

    return True

# Function for winning the game


def win(revealed_word):
    show_new_board(revealed_word)
    print("Congratulations, you guessed correctly!")

    return True

# Interface for the game in the terminal


word, unique_letters = choose_word(words)

while not game_over:
    print('\n' + '*' * 20 + '\n')
    show_new_board(word)
    print('\n')
    print('Incorrect letters: ' + '-'.join(incorrect_letters))
    print(f'Tries: {tries}')
    print('\n' + '*' * 20 + '\n')
    letter = ask_letter()
    tries, over, right_answers = check_letter(letter, word,
                                              tries, right_answers)
    game_over = over
