def string_starts_with_b_and_ends_with_a(word: str, ignore_space: bool = True) -> bool:
    """
    Checks whether a string starts with 'B' and ends with 'A'.

    The comparison is case-insensitive. Optionally, leading and trailing
    whitespace can be ignored before evaluating the string.

    Args:
        word: The string to be evaluated.
        ignore_space: If True, strips leading and trailing whitespace before
            performing the check.

    Returns:
        True if the string starts with 'B' and ends with 'A'; otherwise, False.

    Raises:
        TypeError: If ``word`` is not a string.
    """
    if not isinstance(word, str):
        raise TypeError("word must be a string")

    word = word.strip() if ignore_space else word

    return word.lower().startswith("b") and word.lower().endswith("a")
