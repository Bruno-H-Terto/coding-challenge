from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True, slots=True)
class GameMetrics:
    min_turns: int
    probability: Fraction
    combinations: int


@dataclass(frozen=True, slots=True)
class Roadmap:
    length: int

    def __post_init__(self):
        if self.length < 3:
            raise ValueError("length must be greater than or equal to 3")

    def min_turns(self) -> int:
        return (self.length + 2) // 3

    def probability(self) -> Fraction:
        return Fraction(1, 3) ** self.min_turns()

    def count_combinations(self) -> int:
        """
        Count all possible ways to reach the end of the roadmap.

        A player may advance 1, 2, or 3 positions on each turn. This method
        returns the total number of distinct sequences of moves that exactly
        reach the last position.

        For example, for a roadmap of length 3, there are four possible
        combinations:

            - 1 + 1 + 1
            - 1 + 2
            - 2 + 1
            - 3

        Returns:
            The total number of possible move combinations.
        """
        ways = [0] * (self.length + 1)
        ways[0] = 1

        for position in range(1, self.length + 1):
            ways[position] += ways[position - 1]

            if position >= 2:
                ways[position] += ways[position - 2]

            if position >= 3:
                ways[position] += ways[position - 3]

        return ways[self.length]


def start_the_game(roadmap_length: int) -> GameMetrics:
    """Return game metrics for a roadmap with the given length."""
    roadmap = Roadmap(length=roadmap_length)

    return GameMetrics(
        min_turns=roadmap.min_turns(),
        probability=roadmap.probability(),
        combinations=roadmap.count_combinations(),
    )
