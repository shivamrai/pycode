"""Divisible by 3 - Check if list sum divisible by 3."""


def listsplice(passedlist):
    """listsplice function."""
    total = 0
    for value in passedlist:
        total = total + value
    if total % 3 == 0:
        return 1
    return 0
