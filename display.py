import colorama
from constants import DIM, BLUE
from words import get_random_word
from ascii_art import HANGMAN_STAGES
colorama.init(autoreset=True)


def welcome():print(DIM+ BLUE+r'''
     _                                             
| |                                           
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       ''')



def show_word(secret_word, guessed_letters):

    word= []

    for letter in secret_word:
        if letter in guessed_letters:
            word.append(letter)
        else:
            word.append("_")

    print(" ".join(word))
    
def show_wrong_letters(guessed_letters, secret_word):

    wrong = []

    for l in guessed_letters:
        if l not in secret_word:
            wrong.append(l)

    print(", ".join(wrong))

def show_hangman(lives):
    
    print(HANGMAN_STAGES[lives])

def show_result():
    pass

welcome()