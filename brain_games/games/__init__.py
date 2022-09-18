"""This sumbodule contains game rules / logic.

This top level module contains common settings / components.
"""
from brain_games.cli import get_answer


ROUNDS = 3
SUCCESS_ROUND_MESSAGE = "Correct!"
FAILED_ROUND_MESSAGE = "'{0}' is wrong answer ;(. Correct answer was '{1}'."


def play(game):
    """Execute a brain game module.

    Game module must declare:
    - DESCRIPTION variable with full game description and rules
    - get_round_question_and_answer() function which returns question and
      answer for a round

    Returns True if game is successful and False otherwise.
    """
    print(game.DESCRIPTION)

    for _ in range(ROUNDS):
        question, correct_answer = game.get_round_question_and_answer()
        user_answer = get_answer(question)

        if correct_answer != user_answer:
            print(FAILED_ROUND_MESSAGE.format(user_answer, correct_answer))
            return False

        print(SUCCESS_ROUND_MESSAGE)

    return True
