from random import randint


DESCRIPTION = "What number is missing in the progression?"

MIN_LENGTH = 5
MAX_LENGTH = 12
MISSING_ELEMENT_NOTATION = ".."
MIN_START_VALUE = 0
MAX_START_VALUE = 10
MIN_STEP = 1
MAX_STEP = 20


def get_round_question_and_answer():
    start_value = randint(MIN_START_VALUE, MAX_START_VALUE)
    length = randint(MIN_LENGTH, MAX_LENGTH)
    step = randint(MIN_STEP, MAX_STEP)

    progression = [str(start_value + step * x) for x in range(length)]
    missing_element_index = randint(0, length - 1)
    missing_element_value = progression[missing_element_index]
    progression[missing_element_index] = MISSING_ELEMENT_NOTATION

    question = " ".join(progression)
    answer = str(missing_element_value)
    return question, answer
