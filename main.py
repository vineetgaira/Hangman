
from colorama import Fore,Style
colorama.init(autoreset=True)



from game import start_game, get_guess, update_game, check_win, check_lose, play_again
from display import welcome, show_word, show_wrong_letters, show_hangman,show_result,clear_screen

def main():
    clear_screen()
    welcome()

    playing = True
    while playing:
    
        secret_word, guessed_letters, lives = start_game()
        won = False
        game_over =False
        clear_screen()
        

        while not game_over:
            clear_screen()
            show_word(secret_word,guessed_letters)
            show_wrong_letters(guessed_letters, secret_word)
            show_hangman(lives)

            status=None
            while status != "ok":
                status, guess = get_guess(guessed_letters)
                if status == "invalid":
                    print(Fore.RED+"Invalid input! Please enter a single character.")
                elif status == "repeat":
                    print(Fore.RED+f"You have already guessed the letter {Fore.CYAN+guess}")
            
            guessed_letters,lives=update_game(secret_word, guess, guessed_letters, lives)

            if check_win(secret_word,guessed_letters):
                game_over=True
                won=True
            elif check_lose(lives):
                game_over=True
                won = False
        
        clear_screen()
        show_hangman(lives)
        show_result(won,secret_word)
        playing=play_again()
        if not playing:
            print(Style.BRIGHT+Fore.CYAN+"Thanks for playing....سس")

if __name__ == "__main__":
    main()

                


