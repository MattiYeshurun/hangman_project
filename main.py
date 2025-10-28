from hangman.game import init_state, is_won, is_lost, validate_guess
from hangman.io import print_status, prompt_guess
from hangman.words import choose_secret_word

MAX_TRIES = 6

def play(words: list[str], max_tries: int = MAX_TRIES) -> None:
    secret_word = choose_secret_word(words)
    state = init_state(secret_word, max_tries)
    print("welcome to Hangman")

    while not is_won(state) and not is_lost(state):
        print_status(state)
        
        prompt_guess()






if __name__ == "__main__":




