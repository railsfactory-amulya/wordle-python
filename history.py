import json
from pathlib import Path


class GameHistory:
    """Store completed Wordle games and calculate player statistics."""

    def __init__(self, path: str = "history.jsonl") -> None:
        self.path = Path(path)
        self.games = []
        self.load()

    def load(self) -> None:
        """Load game history from the JSONL file."""
        if not self.path.exists():
            self.games = []
            return
       
        with self.path.open("r", encoding="utf-8") as history_file:
            self.games = [
                json.loads(line)
                for line in history_file
                if line.strip()
            ]

    def save(self, game: dict) -> None:
        """append game to the history JSON file."""

        with self.path.open("a") as history_file:
            history_file.write(
                json.dumps(game) + "\n"
            )

    def record_game(
        self,
        won: bool,
        attempts: int,
        word: str,
    ) -> None:
        """Record a completed game and save the history."""
        game = {
            "won": won,
            "attempts": attempts,
            "word": word,
        }

        self.games.append(game)
        self.save(game)

    @property
    def total_games(self) -> int:
        """Return the number of completed games."""
        return len(self.games)

    @property
    def total_wins(self) -> int:
        """Return the number of games won."""
        return sum(game["won"] for game in self.games)

    @property
    def win_percentage(self) -> float:
        """Return the percentage of games won."""
        if self.total_games == 0:
            return 0

        return (self.total_wins / self.total_games) * 100

    @property
    def current_streak(self) -> int:
        """Return the consecutive wins ending with the latest game."""
        streak = 0

        for game in reversed(self.games):
            if not game["won"]:
                break

            streak += 1

        return streak

    @property
    def best_streak(self) -> int:
        """Return the longest winning streak."""
        best = 0
        current = 0

        for game in self.games:
            if game["won"]:
                current += 1
                best = max(best, current)
            else:
                current = 0

        return best