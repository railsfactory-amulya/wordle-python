import random
from pathlib import Path

from game import MAX_GUESSES, WORD_LENGTH, Game
from history import GameHistory

WORDS_FILE = "words.txt"


def load_words(path: str = WORDS_FILE) -> list[str]:
    """Load and validate five-letter words from a text file."""
    words = [
        line.strip().lower()
        for line in Path(path).read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]

    invalid = [word for word in words if len(word) != WORD_LENGTH]

    if invalid:
        raise ValueError(
            f"Invalid word(s) found; every word must be "
            f"{WORD_LENGTH} letters: {', '.join(invalid)}"
        )

    return words


def play() -> None:
    """Run one complete Wordle game."""
    words = load_words()
    secret = random.choice(words)

    game = Game(secret, words)
    history = GameHistory()

    print("\nWelcome to Wordle!")

    while not game.is_over:
        print()
        print(game)

        guess = input("\nEnter your guess: ")

        try:
            game.make_guess(guess)
        except ValueError as error:
            print(f"Error: {error}")
            continue

    print()
    print(game)

    if game.is_won:
        print(
            f"\nYou got it in "
            f"{len(game.guesses)}/{MAX_GUESSES}!"
        )
    else:
        print(f"\nThe word was {game.secret.upper()}")

    history.record_game(
        won=game.is_won,
        attempts=len(game.guesses),
        word=game.secret,
    )

    print("\n--- Statistics ---")
    print(f"Games played: {history.total_games}")
    print(f"Wins: {history.total_wins}")
    print(f"Win percentage: {history.win_percentage:.1f}%")
    print(f"Current streak: {history.current_streak}")
    print(f"Best streak: {history.best_streak}")


if __name__ == "__main__":
    play()