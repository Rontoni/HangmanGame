"""
Hangman Game 
"""

from random import choice 

# Words for our game 

words = ['motivation', 'appointment', 'discovery', 'caligraphy', 'rendering',]
correct_letters = []
incorrect_letters = []
tries = 6
right_answers = 0 
game_over = False

#Function for picking a word 
def choose_word(list_of_words):
    chosen_word = choice(list_of_words)
    different_letters = len(set(chosen_word))

    return chosen_word, different_letters

#Function for picking a letter
def ask_letter():
    chosen_letter = ''
    is_valid = False
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    while not is_valid:
        chosen_letter = input("Please choose a letter")

        if chosen_letter in alphabet and len(chosen_letter) == 1:
            is_valid = True 
        else: 
            print("You haven't chosen a correct letter")
    
    return chosen_letter

#Function for showing the board while picking words
def show_new_board(chosen_word):
    hidden_list = []

    for l in chosen_word:
        if l in correct_letters: 
            hidden_list.append(l)
        else:
            hidden_list.append('-')
    print(' '.join(hidden_list))

#Function for checking if the letter entered by the player matches the hidden word and tries left
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