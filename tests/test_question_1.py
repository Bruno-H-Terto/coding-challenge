import pytest
from src.question_1 import string_starts_with_b_and_ends_with_a


def test_must_return_true_if_string_starts_with_b_and_ends_with_a():
    word = "BA"

    assert string_starts_with_b_and_ends_with_a(word)


def test_must_return_false_if_string_not_starts_with_b_and_ends_with_a():
    word = "CA"

    assert not string_starts_with_b_and_ends_with_a(word)


def test_must_return_false_if_string_starts_with_b_and_not_ends_with_a():
    word = "BC"

    assert not string_starts_with_b_and_ends_with_a(word)


def test_must_raise_if_word_is_not_a_string():
    word = 123

    with pytest.raises(TypeError):
        string_starts_with_b_and_ends_with_a(word)


def test_must_be_case_insensitive():
    words = ["Bola", "banana", "bOA"]

    assert all(string_starts_with_b_and_ends_with_a(word) for word in words)


def test_must_ignore_spaces():
    word = " BA  "

    assert string_starts_with_b_and_ends_with_a(word)


def test_must_not_ignore_spaces_if_this_ignore_space_value_id_false():
    word = " BA  "

    assert not string_starts_with_b_and_ends_with_a(word, ignore_space=False)
