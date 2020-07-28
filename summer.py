from typing import Union


def summer(*args) -> Union[int, float]:
    total = 0

    for arg in args:
        try:
            total += arg
        except TypeError:
            raise Exception("summer() can only accept int and float args")

    return total
