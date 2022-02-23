from models import Problem, Solution, ScoredSolution


# noinspection PyUnusedLocal
def score_solution(problem: Problem, solution: Solution) -> ScoredSolution:
    score = 0
    return ScoredSolution(
        score=score,
        solution=solution,
    )
