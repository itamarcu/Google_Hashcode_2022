from typing import List
from models import Problem, Solution, Contributor, Project


def parse_input(name: str, input_lines: List[str]) -> Problem:
    line_index = 0
    contributor_count_s, project_count_s = input_lines[line_index].split(' ')
    contributor_count = int(contributor_count_s)
    project_count = int(project_count_s)
    contributors = []
    for c_i in range(contributor_count):
        line_index += 1
        contributor_name, skill_count = input_lines[line_index].split(' ')
        skills = {}
        for s_i in range(int(skill_count)):
            line_index += 1
            skill_name, skill_level_s = input_lines[line_index].split(' ')
            skill_level = int(skill_level_s)
            skills[skill_name] = skill_level
        contributor = Contributor(contributor_name, skills)
        contributors.append(contributor)
    projects = []
    for p_i in range(project_count):
        line_index += 1
        name, di, si, bi, ri = input_lines[line_index].split(' ')
        roles_needed = []
        for r_i in range(int(ri)):
            line_index += 1
            skill_name, skill_level_s = input_lines[line_index].split(' ')
            skill_level = int(skill_level_s)
            roles_needed.append((skill_name, skill_level))
        project = Project(name, int(di), int(si), int(bi), roles_needed)
        projects.append(project)

    return Problem(name, contributors, projects)


def spew_output(solution: Solution) -> List[str]:
    return []
