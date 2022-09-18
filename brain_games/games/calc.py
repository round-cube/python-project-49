from random import choice, randint
from enum import Enum


DESCRIPTION = "What is the result of the expression?"

MIN_NUMBER_VALUE = 0
MAX_NUMBER_VALUE = 30

QUESTION = "{0} {1} {2}"


class Operation(Enum):
    ADD = "+"
    SUB = "-"
    MULT = "*"


def apply_operation(first_number, second_number, operation):
    """Apply operation to first_number and second_number. Return result."""
    if operation == Operation.ADD:
        return first_number + second_number
    elif operation == Operation.SUB:
        return first_number - second_number
    elif operation == Operation.MULT:
        return first_number * second_number
    else:
        raise ValueError("Unsupported operation type")


def get_round_question_and_answer():
    operation = choice(list(Operation))
    first_number = randint(MIN_NUMBER_VALUE, MAX_NUMBER_VALUE)
    second_number = randint(MIN_NUMBER_VALUE, MAX_NUMBER_VALUE)
    question = QUESTION.format(first_number, operation.value, second_number)
    result = apply_operation(first_number, second_number, operation)
    answer = str(result)
    return question, answer
