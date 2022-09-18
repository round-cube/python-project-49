from brain_games.cli import greet_user, welcome_user, say_goodbye
from brain_games.games import play


def run_game_script(game):
    """Greet user, run game and exit."""
    greet_user()
    name = welcome_user()
    game_result = play(game)
    say_goodbye(name, game_result)
