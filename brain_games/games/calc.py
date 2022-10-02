from random import choice, randint
from operator import add, sub, mul


DESCRIPTION = "What is the result of the expression?"

MIN_NUMBER_VALUE = 0
MAX_NUMBER_VALUE = 30

QUESTION = "{0} {1} {2}"


OPERATIONS = {
    "+": add,
    "-": sub,
    "*": mul
}


def apply_operation(first_number, second_number, operation):
    """Apply operation to first_number and second_number. Return result."""
    operation_func = OPERATIONS.get(operation)
    if not operation_func:
        raise ValueError("Unsupported operation type")
    return operation_func(first_number, second_number)


def get_round_question_and_answer():
    operation = choice(list(OPERATIONS.keys()))
    first_number = randint(MIN_NUMBER_VALUE, MAX_NUMBER_VALUE)
    second_number = randint(MIN_NUMBER_VALUE, MAX_NUMBER_VALUE)
    question = QUESTION.format(first_number, operation, second_number)
    result = apply_operation(first_number, second_number, operation)
    answer = str(result)
    return question, answer
