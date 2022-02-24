from models import Problem, Solution
from solvers.parameter_project_sorter import get_sorted_projects
from solvers.solve_by_project_order import solve_by_project_order


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
    solution = solve_by_project_order(problem, sorted_projects)
    print(f'Done, completed {len(solution.projects)}/{len(projects)} projects'
          f' ({len(solution.projects) / len(projects) % .02}%)')
    return solution
