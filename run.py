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

# Function for starting the game with a word 

def choose_word(list_of_words):
    chosen_word = choice(list_of_words)
    different_letters = len(set(chosen_word))

    return chosen_word, different_letters
