# Wordle CLI Game

A command-line version of the popular Wordle game built using Python.

The player has 6 attempts to guess a hidden 5-letter word. After each guess, the game indicates which letters are:

The game also keeps track of completed games and maintains statistics such as wins, win percentage, current streak, and best streak.

## Features

- 6 attempts per game
- 5-letter words
- Validates guesses against a word list
- Correct handling of duplicate letters
- Clear terminal-based game board
- Persistent game history using JSON
- Win percentage and streak statistics
- Input validation with helpful error messages
- Automated tests using pytest
- Code quality checks using Ruff
- Type hints and docstrings

## Requirements

* Python 3.10+
* pytest
* Ruff

## Setup

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install pytest ruff
```

## Running the Game

Start the game with:

```bash
python wordle.py
```

## Running Tests

Run the complete test suite:

```bash
pytest -v
```

## Code Quality

Run Ruff:

```bash
ruff check .
```

The project should have no Ruff warnings or errors.

## Game History

Completed games are stored in:

```text
history.json
```

Each completed game contains:

```json
{
  "won": true,
  "attempts": 5,
  "word": "chess"
}
```

`history.json` is generated automatically and is excluded from Git.

