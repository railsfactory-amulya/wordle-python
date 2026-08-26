MAX_GUESSES = 6
WORD_LENGTH = 5

class GuessResult:
    """Represent the result of a single Wordle guess."""

    CORRECT = "correct"
    PRESENT = "present"
    ABSENT = "absent"

    def __init__(self, guess: str, results: list[str]) -> None:
        self.guess = guess
        self.results = results

    def is_correct(self) -> bool:
        """Return True when every letter is correct."""
        return all(result == self.CORRECT for result in self.results)

    def __str__(self) -> str:
        """Render the guess and its results."""
        symbols = {
            self.CORRECT: "✓",
            self.PRESENT: "~",
            self.ABSENT: "✗",
        }

        letters = "  ".join(self.guess.upper())
        result = "  ".join(symbols[item] for item in self.results)

        return f"{letters}\n{result}"

def evaluate_guess(secret: str, guess: str) -> GuessResult:
    """Evaluate a guess against the secret word."""
    results = [GuessResult.ABSENT] * len(guess)
    remaining = list(secret)

    # First pass: correct-position matches.
    for index, letter in enumerate(guess):
        if letter == secret[index]:
            results[index] = GuessResult.CORRECT
            remaining[index] = None

    # Second pass: present-but-wrong-position matches.
    for index, letter in enumerate(guess):
        if results[index] == GuessResult.CORRECT:
            continue

        if letter in remaining:
            results[index] = GuessResult.PRESENT
            remaining[remaining.index(letter)] = None

    return GuessResult(guess, results)

class Game:
    """Manage one Wordle game."""

    def __init__(self, secret: str, words: list[str]) -> None:
        self.secret = secret
        self.words = words
        self.guesses = []

    def make_guess(self, word: str) -> GuessResult:
        """Validate and record a player's guess."""

        if self.is_over:
            raise ValueError("Game is already over.")

        word = word.strip().lower()

        if len(word) != WORD_LENGTH:
            raise ValueError(
                f"Guess must be {WORD_LENGTH} letters."
            )

        if word not in self.words:
            raise ValueError(
                f"'{word}' is not in the word list."
            )

        result = evaluate_guess(self.secret, word)
        self.guesses.append(result)

        return result

    @property
    def is_won(self) -> bool:
        """Return True when the player has guessed the secret word."""

        return bool(self.guesses) and self.guesses[-1].is_correct()

    @property
    def is_over(self) -> bool:
        """Return True when the game has been won or all attempts are used."""
        return self.is_won or len(self.guesses) >= MAX_GUESSES

    def __str__(self) -> str:
        """Render the current game board."""
        lines = []

        for result in self.guesses:
            lines.append(str(result))
            lines.append("")

        remaining = MAX_GUESSES - len(self.guesses)
        lines.append(f"Attempts remaining: {remaining}")

        return "\n".join(lines)
