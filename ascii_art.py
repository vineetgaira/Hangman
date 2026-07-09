import colorama
from colorama import Fore,Style
colorama.init(autoreset=True)

hangman='''
+---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
'''

print(Style.BRIGHT+Fore.LIGHTYELLOW_EX+hangman)