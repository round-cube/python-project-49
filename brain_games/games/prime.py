from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

MIN_NUMBER_VALUE = 1
MAX_NUMBER_VALUE = 100

YES_ANSWER = "yes"
NO_ANSWER = "no"


def is_prime(n):
    """Check if number is prime."""
    if n <= 1:
        return False

    for i in range(2, int(n / 2) + 1):
        if (n % i) == 0:
            return False
    else:
        return True


def get_round_question_and_answer():
    number = randint(MIN_NUMBER_VALUE, MAX_NUMBER_VALUE)
    question = str(number)
    answer = YES_ANSWER if is_prime(number) else NO_ANSWER
    return question, answer
