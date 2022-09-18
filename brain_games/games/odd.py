import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER_VALUE = 1
MAX_NUMBER_VALUE = 100
YES_ANSWER = "yes"
NO_ANSWER = "no"


def get_round_question_and_answer():
    number = random.randint(MIN_NUMBER_VALUE, MAX_NUMBER_VALUE)
    is_odd = not bool(number % 2)
    correct_answer = YES_ANSWER if is_odd else NO_ANSWER
    return number, correct_answer
