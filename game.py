
from constants import MAX_LIVES
from words import WORDS
from words import get_random_word

def start_game():
    secret_word = get_random_word

    guessed_letters = set()

    lives = MAX_LIVES

    return secret_word, guessed_letters, lives
                    

def get_guess(guessed_letters):

    while True:

        guess = input("Guess a letter :").lower().strip()
        
        if len(guess) !=1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.")
        elif guess in guessed_letters:
            print(f"The letter {guess} is already guessed.")
        else:
            return guess

def update_game():
   pass

def check_win():
    pass

def check_lose():
    pass

def play_again():
    pass

