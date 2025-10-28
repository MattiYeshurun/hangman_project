from hangman.game import render_display, is_won, is_lost, render_summary


def prompt_guess() -> str:
     guess = input("בחר אות בעברית: ")
     return guess


def print_status(state: dict) -> None:
    display_word = render_display(state)
    guessed_letters = state["guessed"]
    tries_left = state["max_tries"] - state["wrong_guesses"]

    print("-" * 30)
    print(f"המצב הנוכחי:   {display_word}")
    print(f"כמות ניחושים שנותרו: {tries_left} מתוך {state["max_tries"]}")
    print(f"האותיות שניחשת הן: {''.join(guessed_letters)}")
    print("-" * 30)

def print_result(state: dict) -> None:
    if is_won(state):
        print("you win!!!")
    elif is_lost(state):
        print("you lost")



