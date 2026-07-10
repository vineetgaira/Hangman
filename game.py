import colorama
from colorama import Fore
from constants import MAX_LIVES
from words import WORDS
from words import get_random_word
colorama.init(autoreset=True)


def start_game():
    pass

def display_progress(feedback_message,guessed_letters,lives):

    secret_word = get_random_word()

    show_word = ["____"]*len(secret_word)

    display_word="  ".join(show_word)
        
    print("==============================")
    print(f"Status: {feedback_message}")
    print("==============================")
    print("\nWord: ", end="")
    print(*display_word)
    print(f"\nLives remaining: {lives}")
    print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}\n")
        
        

def get_guess():

    guessed_letters = set()

    guess = input("Guess a letter :").lower().strip()

    if len(guess) !=1 or not guess.isalpha():
        feedback_message = "Invalid input! Please enter a single letter."
    
    if guess in guessed_letters:
        feedback_message = f"You already guessed the letter {guess}"

    guessed_letters.add(guess)

    return guessed_letters,feedback_message

def update_game():
   pass

def check_win():
    pass

def check_lose():
    pass

def play_again():
    pass

get_guess()