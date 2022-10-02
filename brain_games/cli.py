import prompt


GREET_USER_MESSAGE = "Welcome to the Brain Games!"
NAME_REQUEST_MESSAGE = 'May I have your name? '
WELCOME_MESSAGE = "Hello, {0}!"


def greet_user():
    """Greet user."""
    print(GREET_USER_MESSAGE)


def welcome_user():
    """Ask for a name and print formatted welcome message."""
    name = prompt.string(NAME_REQUEST_MESSAGE)
    welcome_message = WELCOME_MESSAGE.format(name)
    print(welcome_message)
    return name
