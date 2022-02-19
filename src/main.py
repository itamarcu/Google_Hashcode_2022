import os
import time

from src.all_files import ALL_FILES
from parser_and_spewer import parse_input, spew_output

from solvers.empty_solution import solve as empty_solve
from solvers.simple_popularity_solver import solve as simple_solve

INPUTS_DIR = 'inputs'
OUTPUTS_DIR = 'outputs'


def solve_all(file_comment="", solve=empty_solve):
    print("---START---")
    for file_name in ALL_FILES:
        solve_one(file_name, file_comment, solve)
        print('')  # newline
    print("---END---")


def solve_one(file_name: str, file_comment="", solve=empty_solve):
    print(f"reading {file_name}...")
    filepath = f"{INPUTS_DIR}/{file_name}"
    with open(filepath) as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]

    problem = parse_input(file_name, lines)
    print(f"solving...")
    t_start = time.time()
    solution = solve(problem)
    t_end = time.time()
    print(f"took {t_end - t_start} seconds")
    score = solution.score
    output_lines = spew_output(solution)
    print(f"SCORE: {score}")
    file_name = file_name[:file_name.index(".")]
    save_solution(file_name, file_comment, output_lines, score)


def save_solution(file_name: str, file_comment, output_lines, score: int):
    output_file_name = f"{OUTPUTS_DIR}/{file_name}_{file_comment}_{score}.txt"
    assert output_file_name != file_name
    if not os.path.exists(OUTPUTS_DIR):
        os.mkdir(OUTPUTS_DIR)
    with open(output_file_name, "w+") as file:
        for line in output_lines:
            file.write(line + "\n")
    print("-> " + output_file_name)


if __name__ == '__main__':
    solve_all(file_comment="basic", solve=simple_solve)
    # solve_all(file_comment="empty", solve=empty_solve)
    # solve_one(file_name="sample.txt", file_comment="empty", solve=empty_solve)