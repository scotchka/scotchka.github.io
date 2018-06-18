import inspect

BRACKETS = {")": "(", "]": "[", "}": "{"}


def _stack(chars):
    """Push/pop frames to/from call stack."""
    while chars:
        char = chars.pop(0)
        if char in BRACKETS.values():
            _stack(chars)  # push
        elif char in BRACKETS:
            previous = inspect.stack()[1]
            if (
                previous.function != "_stack"
                or previous.frame.f_locals["char"] != BRACKETS[char]
            ):
                raise IndexError
            return  # pop

    if inspect.stack()[1].function == "_stack":  # check no brackets remain
        raise IndexError


def is_balanced(string):
    """Check whether brackets in given string balanced."""
    try:
        _stack(list(string))
    except IndexError:
        return False
    else:
        return True
