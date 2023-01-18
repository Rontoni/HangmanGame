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

# Function for choosing a word 

def choose_word(list_of_words):
    chosen_word = choice(list_of_words)
    different_letters = len(set(chosen_word))

    return chosen_word, different_letters

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
