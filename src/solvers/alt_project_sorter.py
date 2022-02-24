from models import Problem, Project, Skill

from typing import List, Dict, Tuple
from collections import defaultdict
import math


def get_sorted_projects(problem: Problem):
    projects = problem.projects
    contributors = problem.contributors
    contributor_count = len(contributors)
    # required_in_?_projects, level_required_in_?_projects, available_to_?_people, level_available_to_?_people,
    # available_at_level_to_?
    skills = defaultdict(lambda: [0, 0, 0, 0, defaultdict(lambda: 0)])
    for project in projects:
        for role in project.roles_needed:
            skill = role[0]
            skill_stats = skills[skill]
            skill_stats[0] += 1
            skill_stats[1] += role[1]
    for contributor in contributors:
        for skill in contributor.skills:
            skill_stats = skills[skill]
            skill_stats[2] += 1
            skill_stats[3] += contributor.skills[skill]
            for i in range(contributor.skills[skill] * 2):
                if i < contributor.skills[skill] + 2:
                    skill_stats[4][i] += 1
                else:
                    skill_stats[4][i] += 1 / (i - contributor.skills[skill] + 1)
    contributor_usefulness = defaultdict(lambda: 0)
    contributor_indispensability = defaultdict(lambda: 0)
    for contributor in contributors:
        for skill in contributor.skills:
            contributor_usefulness[contributor.name] += contributor.skills[skill] * skills[skill][1]
            contributor_indispensability[contributor.name] += contributor.skills[skill] / skills[skill][3]
    project_difficulty = defaultdict(lambda: 0)
    for project in projects:
        for role in project.roles_needed:
            skill = role[0]
            skill_rarity = skills[skill][4][role[1]] + 1
            project_difficulty[project.name] += len(problem.contributors) / skill_rarity
    average_due_date = sum([project.best_before_date for project in projects]) / len(projects)

    score_dict = [[project.score_reward/(project_difficulty[project.name] * project.days_needed)
                   * (1 + math.log(project.best_before_date / average_due_date)), project] for project in projects]
    score_dict.sort(key=lambda x: x[0])
    return [score_pair[1] for score_pair in score_dict]
    # assumed_day = 0
    # available_contributors = contributor_count
    #
    # for score_pair in score_dict:
