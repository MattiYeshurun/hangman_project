from hangman.game import render_display, is_won, is_lost


def prompt_guess() -> str:
     guess = input("Guess one letter: ")
     return guess


def print_status(state: dict) -> None:
    display_word = render_display(state)[::-1]
    guessed_letters = state["guessed"]
    tries_left = state["max_tries"] - state["wrong_guesses"]

    print("-" * 30)
    print(f"The current word: {display_word}")
    print(f"Remaining guesses: {tries_left} from {state["max_tries"]}")
    print(f"The letters that were guessed: {''.join(guessed_letters)}")
    print("-" * 30)

def print_result(state: dict) -> None:
    if is_won(state):
        print("you win!!!")
    elif is_lost(state):
        print("you lost")



