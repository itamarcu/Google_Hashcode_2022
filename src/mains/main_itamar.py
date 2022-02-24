from src.solvers.solution_with_ordering import solve as solution_with_ordering
# noinspection PyUnresolvedReferences
from src.run_solution import solve_one, solve_all

if __name__ == '__main__':
    # solve_one(file_name="a_an_example.in.txt", file_comment="swo", solve=solution_with_ordering)
    solve_all(file_comment="swo", solve=solution_with_ordering)
