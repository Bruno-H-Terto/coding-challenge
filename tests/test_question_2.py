from src.question_2 import last_sequence_term
import pytest


def test_must_return_a_term_position_of_arithmetic_sequence():
    first_term = last_sequence_term(first_term=11, common_difference=7, term_position=1)
    second_term = last_sequence_term(
        first_term=11, common_difference=7, term_position=2
    )
    ninth_hundred_ninety_ninth_term = last_sequence_term(
        first_term=11, common_difference=7, term_position=999
    )

    assert first_term == 11
    assert second_term == 18
    assert ninth_hundred_ninety_ninth_term == 6997


def test_must_be_raise_if_term_position_is_lower_than_1():
    with pytest.raises(ValueError):
        last_sequence_term(first_term=11, common_difference=7, term_position=-1)
