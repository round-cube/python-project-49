import random
import prompt


GAME_ROUNDS = 3
START_GAME_MESSAGE = ('Answer "yes" if the number is even, '
                      'otherwise answer "no".')
MIN_NUMBER_VALUE = 1
MAX_NUMBER_VALUE = 100
NUMBER_QUESTION = "Question: {0}"
ANSWER_MESSAGE = "Your answer: "
YES_ANSWER = "yes"
NO_ANSWER = "no"
RESPONSE_TO_CORRECT = "Correct!"
RESPONSE_TO_ERROR = "Let's try again, {0}"
SUCCESS_MESSAGE = "Congratulations, {0}!"


def prompt_number_and_check_result():
    """Generate number, and prompt a result.

    Returns True if result is correct, False otherwise.
    """
    number = random.randint(MIN_NUMBER_VALUE, MAX_NUMBER_VALUE)
    is_odd = not bool(number % 2)
    correct_answer = YES_ANSWER if is_odd else NO_ANSWER
    question = NUMBER_QUESTION.format(number)
    print(question)
    answer = prompt.string(ANSWER_MESSAGE)
    lower_answer = answer.lower()
    return lower_answer == correct_answer


def print_round_message(round_is_successful, name):
    """Prints message after round for user with given name."""
    if round_is_successful:
        print(RESPONSE_TO_CORRECT)
    else:
        response_to_error = RESPONSE_TO_ERROR.format(name)
        print(response_to_error)


def play_odd_game(name):
    """Play game of guessing the oddity for user with given name."""
    print(START_GAME_MESSAGE)

    for _ in range(GAME_ROUNDS):
        round_is_successful = prompt_number_and_check_result()
        print_round_message(round_is_successful, name)
        if not round_is_successful:
            return

    success_message = SUCCESS_MESSAGE.format(name)
    print(success_message)
