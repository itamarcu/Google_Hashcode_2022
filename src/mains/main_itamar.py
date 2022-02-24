from src.solvers.solution_3_retrying_projects_later import solve as solution_attempt_3
# noinspection PyUnresolvedReferences
from src.run_solution import solve_one, solve_all

if __name__ == '__main__':
    # solve_one(file_name="a_an_example.in.txt", file_comment="swo", solve=solution_attempt_3)
    solve_all(file_comment="s3", solve=solution_attempt_3)
