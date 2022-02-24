import all_input_files
from src.solvers.solution_3_retrying_projects_later import solve as solution_attempt_3
# noinspection PyUnresolvedReferences
from src.run_solution import solve_one, solve_all

if __name__ == '__main__':
    solve_one(file_name=all_input_files.ALL_FILES[4], file_comment="s3_s1", solve=solution_attempt_3)
    # solve_all(file_comment="s3", solve=solution_attempt_3)
