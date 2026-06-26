from fractions import Fraction
import pytest

from src.question_3 import start_the_game


def expected_min_turns(length: int) -> int:
    return (length + 2) // 3


def expected_probability(length: int) -> Fraction:
    return Fraction(1, 3) ** expected_min_turns(length)


def expected_combinations(remaining: int) -> int:
    if remaining == 0:
        return 1

    if remaining < 0:
        return 0

    return sum(expected_combinations(remaining - step) for step in (1, 2, 3))


@pytest.mark.parametrize("length", range(3, 20))
def test_must_return_correct_metrics_for_several_lengths(length: int):
    metrics = start_the_game(length)

    assert metrics.min_turns == expected_min_turns(length)
    assert metrics.probability == expected_probability(length)
    assert metrics.combinations == expected_combinations(length)


@pytest.mark.parametrize("length", [0, 1, 2, -1])
def test_must_raise_if_length_is_lower_than_3(length: int):
    with pytest.raises(ValueError):
        start_the_game(length)


def test_must_return_metrics_in_trivial_case():
    metrics = start_the_game(3)

    assert metrics.min_turns == 1
    assert metrics.probability == Fraction(1, 3)
    assert metrics.combinations == 4
