from src.run_solution import solve_one, solve_all
from src.solvers.empty_solution import solve as empty_solve

if __name__ == '__main__':
    solve_all(file_comment="empty", solve=empty_solve)
    solve_one(file_name="a.txt", file_comment="empty", solve=empty_solve)
