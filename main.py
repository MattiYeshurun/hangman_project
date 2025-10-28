from hangman.game import init_state, is_won, is_lost, validate_guess, render_display, apply_guess, render_summary
from hangman.io import print_status, prompt_guess, print_result
from hangman.words import choose_secret_word
from data.words import words



MAX_TRIES = 6

def play(words: list[str], max_tries: int = MAX_TRIES) -> None:
    secret_word = choose_secret_word(words)
    state = init_state(secret_word, max_tries)
    print("ברוכים הבאים למשחק Hangman")

    while not is_won(state) and not is_lost(state):

        print_status(state)
        render_display(state)
        p = prompt_guess()
        validate_guess(p, state["guessed"])
        apply_guess(state, p)
    print(render_summary(state))
    print_result(state)

if __name__ == "__main__":
    play(words, MAX_TRIES)









