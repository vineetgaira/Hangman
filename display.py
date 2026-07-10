import colorama
from colorama import Fore, Style
from ascii_art import HANGMAN_STAGES
colorama.init(autoreset=True)

def clear_screen():
    print("\033[H\033[J", end="")

def welcome():print(Fore.BLUE+r'''
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

    print(Style.BRIGHT+Fore.BLUE+" ".join(word))
    
def show_wrong_letters(guessed_letters, secret_word):

    wrong = []

    for l in guessed_letters:
        if l not in secret_word:
            wrong.append(l)

    print(Fore.RED+", ".join(wrong))

def show_hangman(lives):

    print(Fore.BLUE+HANGMAN_STAGES[lives])

def show_result(won, secret_word):
    if won:
        print(Fore.GREEN+f"Congratulations!\nYou Win!\nThe word was {secret_word}")
    else:
        print(Fore.RED+f"Game Over!\nThe word was {Fore.GREEN+secret_word}")
    

