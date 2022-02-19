from typing import List
from models import Problem, Solution, Client


# noinspection PyPep8Naming
def parse_input(name: str, input_lines: List[str]) -> Problem:
    client_count = int(input_lines[0])
    clients = []
    ingredients = set()
    for i in range(client_count):
        likes = set(input_lines[2 * i + 1].split()[1:])
        dislikes = set(input_lines[2 * i + 2].split()[1:])
        clients.append(Client(likes=likes, dislikes=dislikes))
        ingredients.update(likes)
        ingredients.update(dislikes)
    return Problem(
        name=name,
        clients=clients,
        ingredients=ingredients
    )


def spew_output(solution: Solution) -> List[str]:
    line = ' '.join(list(solution.pizza))
    return [line]
