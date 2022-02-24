from collections import defaultdict

from models import Problem, Solution, ScoredSolution


# noinspection PyUnusedLocal
def score_solution(problem: Problem, solution: Solution) -> ScoredSolution:
    score = 0
    contributor_availability = defaultdict(lambda: 0)
    for i in range(len(solution.projects)):
        project = solution.projects[i]
        contributors = solution.contributors[i]
        start_time = max([contributor_availability[contributor.name] for contributor in contributors])
        end_time = start_time + project.days_needed
        for contributor in contributors:
            contributor_availability[contributor.name] = end_time
        score += max(0, project.score_reward - min(0, end_time - project.best_before_date))
    return ScoredSolution(
        score=score,
        solution=solution,
    )
