import importlib.util
import os
import sys
from unittest.mock import patch

import pytest

MODULE_PATH = os.path.join(os.path.dirname(__file__), "starter-code.py")
spec = importlib.util.spec_from_file_location("starter_code", MODULE_PATH)
starter_code = importlib.util.module_from_spec(spec)
sys.modules["starter_code"] = starter_code
spec.loader.exec_module(starter_code)


def test_welcome_message():
    with patch("builtins.input", side_effect=["Alice", "25", "blue"]):
        result = starter_code.welcome_message()
    assert result == "Hello, Alice! You are 25 years old and your favorite color is blue."


def test_add_two_numbers():
    with patch("builtins.input", side_effect=["3", "7"]):
        result = starter_code.add_two_numbers()
    assert result == 10


def test_add_two_numbers_with_floats():
    with patch("builtins.input", side_effect=["2.5", "1.5"]):
        result = starter_code.add_two_numbers()
    assert result == 4.0


@pytest.mark.parametrize(
    "number, expected",
    [
        (4, True),
        (5, False),
        (0, True),
        (-2, True),
        (-3, False),
    ],
)
def test_is_even(number, expected):
    assert starter_code.is_even(number) == expected
