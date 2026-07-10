
from constants import MAX_LIVES
from words import WORDS
from words import get_random_word

def start_game():
    secret_word = get_random_word()

    guessed_letters = set()

    lives = MAX_LIVES

    return secret_word, guessed_letters, lives
                    

def get_guess(guessed_letters):

    while True:
        guess = input("Guess a letter :").lower().strip()
        if len(guess) !=1 or not guess.isalpha():
            return "invalid", guess
        elif guess in guessed_letters:
            return "repeat", guess
        else:
            return "ok", guess
        
def update_game(secret_word, guess, guessed_letters, lives):
    
    if guess not in guessed_letters:
        guessed_letters.add(guess)

    if guess not in secret_word:
        lives-=1

    return guessed_letters,lives

def check_win(secret_word,guessed_letters):
        
        return set(secret_word)<= guessed_letters

def check_lose():
    


def play_again():
    pass

