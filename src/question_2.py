def last_sequence_term(
    first_term: int, common_difference: int, term_position: int
) -> int:
    """
    Return the term at a given position in an arithmetic progression.

    Args:
        first_term: The first term of the arithmetic progression.
        common_difference: The constant difference between consecutive terms.
        term_position: The position of the term in the sequence, starting at 1.

    Returns:
        The term at the given position.

    Raises:
        ValueError: If term_position is lower than 1.
    """
    if term_position < 1:
        raise ValueError("term_position must be greater than or equal to 1")

    return first_term + common_difference * (term_position - 1)
