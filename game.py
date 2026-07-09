import requests
import colorama
from colorama import Fore
from constants import MAX_LIVES
from words import WORDS
from words import get_random_word
colorama.init(autoreset=True)


def start_game():
    pass

def display_progress():
    pass    

def get_guess():
    guessed_letters = set()

    guess = input("Guess a letter :").lower().strip()

    if len(guess) !=1 or not guess.isalpha():
        print("Invalid input! Please enter a single letter.")
    
    if guess in guessed_letters:
        print(f"You already guessed the letter {guess}")

    guessed_letters.add(guess)

def update_game():
    pass

def check_win():
    pass

def check_lose():
    pass

def play_again():
    pass

get_guess()