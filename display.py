import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)
from game import get_random_word


def welcome():print(Style.DIM+Fore.BLUE+r'''
     _                                             
| |                                           
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       ''')



def show_word():
    pass

def show_wrong_letters():
    pass

def show_hangman():
    pass

def show_result():
    pass

welcome()
print(show_word())