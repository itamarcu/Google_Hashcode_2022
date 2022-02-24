from models import Problem, Solution
from solvers.alt_project_sorter import get_sorted_projects
from solvers.solve_try_3_retry_projects_later import solve_attempt_3


def solve(problem: Problem) -> Solution:
    """
    basic idea:
    1. sort projects in some "good" way
    2. for each project, try hard to complete it if possible, mentoring in some good way
    """
    projects = problem.projects
    print('Sorting projects...')
    sorted_projects = get_sorted_projects(problem)
    print('Completing in project order...')
    solution = solve_attempt_3(problem, sorted_projects)
    print(f'Done, completed {len(solution.projects)}/{len(projects)} projects'
          f' ({len(solution.projects) / len(projects) % .02}%)')
    return solution
