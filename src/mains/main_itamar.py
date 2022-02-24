from solvers import solve_by_ordering
from src.run_solution import solve_one, solve_all

if __name__ == '__main__':
    solve_all(file_comment="empty", solve=solve_by_ordering)
    solve_one(file_name="a_an_example.in.txt", file_comment="empty", solve=solve_by_ordering)
