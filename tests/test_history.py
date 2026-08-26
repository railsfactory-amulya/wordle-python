from history import GameHistory


def test_history_file_created(tmp_path):
    history_file = tmp_path / "history.json"

    history = GameHistory(history_file)

    history.record_game(
        won=True,
        attempts=4,
        word="apple",
    )

    assert history_file.exists()


def test_total_games_and_wins(tmp_path):
    history = GameHistory(tmp_path / "history.json")

    history.record_game(True, 4, "apple")
    history.record_game(False, 6, "house")
    history.record_game(True, 3, "plant")

    assert history.total_games == 3
    assert history.total_wins == 2


def test_win_percentage(tmp_path):
    history = GameHistory(tmp_path / "history.json")

    history.record_game(True, 4, "apple")
    history.record_game(False, 6, "house")
    history.record_game(True, 3, "plant")
    history.record_game(True, 5, "table")

    assert history.win_percentage == 75.0


def test_current_streak(tmp_path):
    history = GameHistory(tmp_path / "history.json")

    history.record_game(True, 4, "apple")
    history.record_game(True, 3, "house")
    history.record_game(False, 6, "plant")
    history.record_game(True, 4, "table")
    history.record_game(True, 5, "chair")

    assert history.current_streak == 2


def test_best_streak(tmp_path):
    history = GameHistory(tmp_path / "history.json")

    history.record_game(True, 4, "apple")
    history.record_game(True, 3, "house")
    history.record_game(False, 6, "plant")
    history.record_game(True, 4, "table")
    history.record_game(True, 5, "chair")
    history.record_game(True, 4, "world")

    assert history.best_streak == 3

def test_history_loads_existing_games(tmp_path):
    history_file = tmp_path / "history.json"

    history = GameHistory(history_file)
    history.record_game(True, 4, "apple")
    history.record_game(False, 6, "house")

    new_history = GameHistory(history_file)

    assert new_history.total_games == 2
    assert new_history.total_wins == 1