import importlib.util
import os
import sys
from unittest.mock import patch

MODULE_PATH = os.path.join(os.path.dirname(__file__), "starter-code.py")
spec = importlib.util.spec_from_file_location("starter_code", MODULE_PATH)
starter_code = importlib.util.module_from_spec(spec)
sys.modules["starter_code"] = starter_code
spec.loader.exec_module(starter_code)


def test_win_when_all_letters_guessed_correctly():
    messages = []
    guesses = iter(["p", "y", "t", "h", "o", "n"])
    result = starter_code.play_hangman(
        word_list=["python"],
        guesser=lambda _: next(guesses),
        on_progress=messages.append,
    )
    assert result is True
    assert any("You win!" in m for m in messages)


def test_lose_when_max_incorrect_guesses_reached():
    messages = []
    guesses = iter(["z", "x", "q", "j", "v", "k"])
    result = starter_code.play_hangman(
        word_list=["python"],
        max_incorrect=6,
        guesser=lambda _: next(guesses),
        on_progress=messages.append,
    )
    assert result is False
    assert any("You lose!" in m for m in messages)


def test_repeated_guess_does_not_count_as_incorrect():
    messages = []
    guesses = iter(["z", "z", "p", "y", "t", "h", "o", "n"])
    result = starter_code.play_hangman(
        word_list=["python"],
        max_incorrect=2,
        guesser=lambda _: next(guesses),
        on_progress=messages.append,
    )
    assert result is True
    assert any("already guessed" in m for m in messages)


def test_invalid_guess_is_ignored():
    messages = []
    guesses = iter(["", "12", "ab", "p", "y", "t", "h", "o", "n"])
    result = starter_code.play_hangman(
        word_list=["python"],
        guesser=lambda _: next(guesses),
        on_progress=messages.append,
    )
    assert result is True


def test_uses_random_choice_from_word_list():
    with patch("starter_code.random.choice", return_value="python") as mock_choice:
        messages = []
        guesses = iter(["p", "y", "t", "h", "o", "n"])
        starter_code.play_hangman(
            word_list=starter_code.words,
            guesser=lambda _: next(guesses),
            on_progress=messages.append,
        )
        mock_choice.assert_called_once_with(starter_code.words)
