import requests
import random
import colorama
from colorama import Fore
from constants import MAX_LIVES, VALID_LETTERS
from words import WORDS
colorama.init(autoreset=True)


def start_game():
    pass

def get_word_from_api():

    try:
        url="https://random-word-api.herokuapp.com/word" 
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        word=data[0].upper()
    except requests.exceptions.RequestException as e:
        print(Fore.RED+f"Error: {e}")
        return 0
    return word

def get_random_word():
    try:
        word=get_word_from_api()
    except:
        word=random.choice(WORDS)
    word.upper()
    return word

def display_progress():
    pass

def get_guess():
    pass

def update_game():
    pass

def check_win():
    pass

def check_lose():
    pass

def play_again():
    pass

print(get_random_word())