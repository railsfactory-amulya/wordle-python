import pytest

from game import MAX_GUESSES, Game, GuessResult, evaluate_guess


def test_evaluate_guess_fully_correct():
    result = evaluate_guess("apple", "apple")

    assert result.results == [
        GuessResult.CORRECT,
        GuessResult.CORRECT,
        GuessResult.CORRECT,
        GuessResult.CORRECT,
        GuessResult.CORRECT,
    ]

def test_evaluate_guess_mixed_results():
    result = evaluate_guess("apple", "ample")

    assert result.results == [
        GuessResult.CORRECT,
        GuessResult.ABSENT,
        GuessResult.CORRECT,
        GuessResult.CORRECT,
        GuessResult.CORRECT,
    ]

def test_evaluate_guess_duplicate_letters():
    result = evaluate_guess("spine", "speed")

    assert result.results == [
        GuessResult.CORRECT,
        GuessResult.CORRECT,
        GuessResult.PRESENT,
        GuessResult.ABSENT,
        GuessResult.ABSENT,
    ]


def test_make_guess_rejects_word_not_in_word_list():
    words = ["apple", "house", "river"]

    game = Game("apple", words)

    with pytest.raises(ValueError):
        game.make_guess("xxxxx")


def test_game_is_won_after_correct_guess():
    words = ["apple", "house", "river"]

    game = Game("apple", words)
    game.make_guess("apple")

    assert game.is_won is True


def test_game_is_over_after_six_failed_guesses():
    words = ["apple", "house", "river"]

    game = Game("apple", words)

    for _ in range(MAX_GUESSES):
        game.make_guess("house")

    assert game.is_over is True