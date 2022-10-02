"""Game core engine functions."""
from brain_games.cli import greet_user, welcome_user
import prompt


QUESTION_MESSAGE = "Question: {0}"
ANSWER_MESSAGE = "Your answer: "
SUCCESSFUL_MESSAGE = "Congratulations, {0}!"
FAILED_MESSAGE = "Let's try again, {0}!"

ROUNDS = 3
SUCCESS_ROUND_MESSAGE = "Correct!"
FAILED_ROUND_MESSAGE = "'{0}' is wrong answer ;(. Correct answer was '{1}'."


def get_answer(question):
    """Print question, read user input and return answer."""
    print(QUESTION_MESSAGE.format(question))
    answer = prompt.string(ANSWER_MESSAGE)
    lower_answer = answer.lower()
    return lower_answer


def say_goodbye(name, is_successful):
    """Print final message for event to user with provided name."""
    message = (SUCCESSFUL_MESSAGE.format(name) if is_successful
               else FAILED_MESSAGE.format(name))
    print(message)


def run_game_script(game):
    """Greet user, run game and exit."""
    greet_user()
    name = welcome_user()
    game_result = play(game)
    say_goodbye(name, game_result)


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
