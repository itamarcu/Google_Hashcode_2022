from typing import List

from models import Problem, Project, Solution


def solve_by_project_order(problem: Problem, sorted_projects: List[Project]) -> Solution:
    completed_projects = []
    contributors_by_project = []
    return Solution(
        completed_projects,
        contributors_by_project
    )
