#!/usr/bin/env python3
from brain_games.cli import greet_user, welcome_user
from brain_games.odd_game import play_odd_game


def main():
    greet_user()
    name = welcome_user()
    play_odd_game(name)


if __name__ == "__main__":
    main()
