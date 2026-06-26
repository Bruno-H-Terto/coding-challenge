from src.question_2 import last_sequence_term
import pytest


def test_must_return_a_term_position_of_arithmetic_sequence():
    assert last_sequence_term(11, 7, 1) == 11
    assert last_sequence_term(11, 7, 2) == 18
    assert last_sequence_term(11, 7, 200) == 1404
    assert last_sequence_term(11, 7, 254) == 1782
    assert last_sequence_term(11, 7, 3_542_158) == 24_795_110


def test_must_be_raise_if_term_position_is_lower_than_1():
    with pytest.raises(ValueError):
        last_sequence_term(first_term=11, common_difference=7, term_position=-1)
