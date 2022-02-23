from dataclasses import dataclass


@dataclass
class Problem:
    """
    name of the problem file.
    """
    name: str


@dataclass
class Solution:
    pass


@dataclass
class ScoredSolution:
    solution: Solution
    score: int
