"""Logic of the brain even game."""

from random import randint

RULES = 'Answer "yes" if number even otherwise answer "no".'


def set_parameters():
    """Set parameters to play.

    Returns:
        random number from 1 to 100
    """
    return randint(1, 100)


def ask_question(parts):
    """Ask a question to user.

    Args:
        parts: parameters to play
    """
    print('Question: {p}'.format(p=parts))


def get_correct_answer(parts):
    """Take a parameter to play (number) and check if it is even.

    Args:
        parts: parameters to play

    Returns:
        yes or no, depends on is number even or not
    """
    return 'yes' if (parts % 2 == 0) else 'no'
