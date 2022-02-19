from typing import List
from models import Problem, Solution


# noinspection PyPep8Naming
def parse_input(name: str, input_lines: List[str]) -> Problem:
    return Problem(
        name=name,
    )


def spew_output(solution: Solution) -> List[str]:
    return []
