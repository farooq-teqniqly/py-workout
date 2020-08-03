from typing import Generator

_vowels = ["a", "e", "i", "o", "u"]


def _ensure_not_null(s: str):
    if s is None or len(s.strip()) == 0:
        raise ValueError("Input string cannot be None or empty.")


def english_to_pig_latin(s: str) -> Generator[str, None, None]:
    _ensure_not_null(s)

    words = s.split(" ")

    for word in words:
        if word[0] in _vowels:
            yield word + "way"
        else:
            yield word[1:] + word[0] + "ay"


def english_to_ubbi_dubbi(s: str) -> Generator[str, None, None]:
    _ensure_not_null(s)

    words = s.split(" ")
    for word in words:
        ubbi_dubbi = ""

        for letter in word:
            if letter in _vowels:
                ubbi_dubbi += "ub" + letter
            else:
                ubbi_dubbi += letter

        yield ubbi_dubbi
