
from models import Problem

def get_sorted_projects(problem: Problem):
    projects = problem.projects
    return sorted(projects, key=lambda project: project.score_reward, reverse=True)
