from collections import defaultdict

from models import Problem, Project

LATEFINISHFACTOR = 1.5
EARLYFINISHFACTOR = 0.3
CONTRIBUTORPENALTY = 0.3
LEVELPENALTY = 0.05
IMPROVEMENTITERATIONS = 10
CONTRIBUTORDIVISIONFACTOR = 0.8


def get_sorted_projects(problem: Problem):
    projects = problem.projects
    contributors = problem.contributors
    contributor_count = len(contributors)
    score_dict = [[project.score_reward, project] for project in projects]
    score_dict.sort(key=lambda x: x[0], reverse=True)
    for _ in range(IMPROVEMENTITERATIONS):
        assumed_day = 0
        available_contributors = contributor_count
        contributor_availability = defaultdict(lambda: 0)
        for score_pair in score_dict:
            project = score_pair[1]
            score_pair[0] = project.score_reward
            needed_contributors = len(project.roles_needed)
            while available_contributors < needed_contributors:
                assumed_day += 1
                available_contributors += contributor_availability[assumed_day]
            available_contributors -= needed_contributors
            contributor_availability[assumed_day + project.days_needed] += needed_contributors
            if assumed_day > project.best_before_date:
                score_pair[0] -= LATEFINISHFACTOR * (assumed_day - project.best_before_date)
            else:
                score_pair[0] -= EARLYFINISHFACTOR * (project.best_before_date - assumed_day)
            score_pair[0] -= LEVELPENALTY * sum([role[1] for role in project.roles_needed])
            if score_pair[0] > 0:
                score_pair[0] = score_pair[0] / (CONTRIBUTORDIVISIONFACTOR * contributor_count)
            else:
                score_pair[0] -= CONTRIBUTORPENALTY*contributor_count
        score_dict.sort(key=lambda x: x[0], reverse=True)
    return [score_pair[1] for score_pair in score_dict]
