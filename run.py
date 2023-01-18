"""
Hangman Game 
"""

from random import choice 

# Words for our game 

words = ['motivation', 'appointment', 'discovery', 'caligraphy', 'rendering', 'linguistics', 'preposterous']
correct_letters = []
incorrect_letters = []
tries = 6
right_answers = 0 
game_over = False


