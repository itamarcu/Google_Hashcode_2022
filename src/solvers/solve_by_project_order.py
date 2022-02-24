from collections import defaultdict
from typing import List, Tuple, Optional

from models import Problem, Project, Solution, Contributor, Skill

RoleSlot = Tuple[int, Skill, int, Optional[Contributor], bool]
MAX_DAYS = 100000

def try_fitting_contributor(contributor: Contributor, role_slots: List[RoleSlot])\
        -> Tuple[int, bool]:
    # returns (role_index, will_be_mentored)
    for role_index, skill_name, skill_level_needed, existing_contributor, has_mentor in role_slots:
        if existing_contributor:
            continue
        contributor_skill = contributor.skills.get(skill_name, 0)
        if has_mentor and contributor_skill == skill_level_needed - 1:
            return role_index, True
        if contributor_skill == skill_level_needed:
            return role_index, False
    return -1, False


def solve_by_project_order(problem: Problem, sorted_projects: List[Project]) -> Solution:
    """NOTE: contributors will mutate during this, having skill levels increased"""
    now = 0
    ongoing_project_dates: List[int] = []
    available_contributors = problem.contributors
    contributors_available_by_date = defaultdict(lambda: [])
    completed_projects = []
    contributors_by_project = []
    i_project = -1
    while i_project < len(sorted_projects) and now < MAX_DAYS:
        i_project += 1
        project = sorted_projects[i_project]
        completion_date = now + project.days_needed
        score = max(0, project.score_reward - min(0, completion_date - project.best_before_date))
        if score == 0:
            # cancel project, too late
            continue
        # we need one for every role
        role_slots: List[RoleSlot] = [
            # (role_index, skill_name, skill_level_needed, contributor?, has_mentor)
            (i, name, level, None, False) for i, (name, level) in enumerate(project.roles_needed)
        ]
        successful = False
        for contributor in available_contributors:
            fit_idx, is_mentored = try_fitting_contributor(contributor, role_slots)
            if fit_idx != -1:
                # add this contributor
                role_slots[fit_idx] = (
                    fit_idx, role_slots[fit_idx][1], role_slots[fit_idx][2], contributor, is_mentored
                )
                empty_slots_left = False
                for i in range(len(role_slots)):
                    ri, sn, sl, c, hm = role_slots[i]
                    if not c:
                        empty_slots_left = True
                        # allow this contributor to mentor others
                        if not hm and contributor.skills.get(sn, 0) >= sl:
                            hm = True
                            role_slots[i] = ri, sn, sl, c, hm
                if not empty_slots_left:
                    successful = True
                    break
        if successful:
            # project ready to start
            contributors_here = []
            for i in range(len(role_slots)):
                ri, sn, sl, c, hm = role_slots[i]
                available_contributors.remove(c)
                contributors_available_by_date[completion_date].append(c)
                contributors_here.append(c)
                # level up!
                if c.skills.get(sn, 0) <= sl:
                    c.skills[sn] = c.skills.get(sn, 0) + 1
            sorted_projects.remove(project)
            ongoing_project_dates.append(completion_date)
            completed_projects.append(project)
            contributors_by_project.append(contributors_here)
            print(f"Project {project.name} will complete at {completion_date}")
        else:
            # not possible to complete the project
            # wait day by day!
            while now < MAX_DAYS:
                now = now + 1
                released_contribs = contributors_available_by_date.pop(now, [])
                if released_contribs:
                    available_contributors.extend(released_contribs)
                    break
            print(f"Waited until day {now}")
            # retry this project next loop
            i_project -= 1

    return Solution(
        completed_projects,
        contributors_by_project
    )
