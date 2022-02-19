class Problem:
    """
    name of the problem file.
    """
    name: str

    def __init__(
            self,
            name: str,
    ):
        self.name = name


class Solution:
    """score will be -1 if we don't know what it is"""
    score: int

    def __init__(
            self,
            score: int,
    ):
        self.score = score
