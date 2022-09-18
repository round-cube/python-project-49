from random import randint
from math import gcd


DESCRIPTION = "Find the greatest common divisor of given numbers."


MIN_NUMBER_VALUE = 1
MAX_NUMBER_VALUE = 100


def get_round_question_and_answer():
    first_number = randint(MIN_NUMBER_VALUE, MAX_NUMBER_VALUE)
    second_number = randint(MIN_NUMBER_VALUE, MAX_NUMBER_VALUE)
    numbers_gcd = gcd(first_number, second_number)
    question = f"{first_number} {second_number}"
    answer = str(numbers_gcd)
    return question, answer
