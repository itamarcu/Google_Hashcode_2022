from models import Problem, Project


def get_sorted_projects(problem: Problem):
    projects = problem.projects
    contributors = problem.contributors
    contributor_count = len(contributors)
    score_dict = [[project.score_reward, project] for project in projects]
    score_dict.sort(key=lambda x: x[0])
    return [score_pair[1] for score_pair in score_dict]
    # assumed_day = 0
    # available_contributors = contributor_count
    #
    # for score_pair in score_dict:
