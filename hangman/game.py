from data.words import is_alpha

def init_state(secret: str, max_tries: int) -> dict:
    state = {
        "secret": secret,
        "display": ["_"] * len(secret),
        "guessed": set(),
        "wrong_guesses": 0,
        "max_tries": max_tries
    }
    return state


def validate_guess(ch: str, guessed: set[str]) -> tuple[bool, str]:
    if len(ch) != 1 or not ch in is_alpha:
        return False, "יש להכניס תו בודד!"
    elif ch in guessed:
        return False, f"האות שהכנסת  {ch} נבחרה כבר, בחר אות אחרת "
    return True, ""


def apply_guess(state: dict, ch: str) -> bool:
    state["guessed"].add(ch)
    secret_word = state["secret"]


    for i, secret_char in enumerate(secret_word):
        if secret_char == ch:
            state["display"][i] = ch
            return True
    state["wrong_guesses"] += 1
    return False


def is_won(state: dict) -> bool:
    return "_" not in state["display"]


def is_lost(state: dict) -> bool:
    return state["wrong_guesses"] >= state["max_tries"]

def render_display(state: dict) -> str:
    return "".join(state["display"])

def render_summary(state: dict) -> str:
    return (
        f"המילה הסודית היא: {state["secret"]}\n"
        f"האותיות שניחשת הן: {','.join(state["guessed"])}" )


