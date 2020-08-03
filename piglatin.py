from typing import Generator


def pig_latinize(s: str) -> Generator[str, None, None]:
    if s is None or len(s.strip()) == 0:
        raise ValueError("Input string cannot be None or empty.")

    words = s.split(" ")

    for word in words:
        if word[0] in ["a", "e", "i", "o", "u"]:
            yield word + "way"
        else:
            yield word[1:] + word[0] + "ay"
