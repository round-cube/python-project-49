import prompt


GREET_USER_MESSAGE = "Welcome to the Brain Games!"
NAME_REQUEST_MESSAGE = 'May I have your name? '
WELCOME_MESSAGE = "Hello, {0}!"
QUESTION_MESSAGE = "Question: {0}"
ANSWER_MESSAGE = "Your answer: "
SUCCESSFUL_MESSAGE = "Congratulations, {0}!"
FAILED_MESSAGE = "Let's try again, {0}!"


def greet_user():
    """Greet user."""
    print(GREET_USER_MESSAGE)


def welcome_user():
    """Ask for a name and print formatted welcome message."""
    name = prompt.string(NAME_REQUEST_MESSAGE)
    welcome_message = WELCOME_MESSAGE.format(name)
    print(welcome_message)
    return name


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
