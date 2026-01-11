from pathlib import Path
from math import prod


def read_file(file_name: Path) -> tuple[list[int], list[str]]:
    path = Path(file_name)
    operator_indices = []
    lines = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                lines.append(line.rstrip("\n"))
                if line[0] == "+" or line[0] == "*":
                    for idx, chr in enumerate(line):
                        if chr == "+" or chr == "*":
                            operator_indices.append(idx)
        return (operator_indices, lines)
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: {path} not found")


def get_real_numbers(numbers: list[int]) -> list[int]:
    real_numbers: list[int] = []

    return real_numbers

def get_grand_total(instructions: list[list[str]]) -> int:
    total = 0
    for col_idx in range(len(instructions[0])):
        problem = []
        for idx in range(len(instructions)):
            if instructions[idx][col_idx] == "*":
                total += prod(problem)
            elif instructions[idx][col_idx] == "+":
                total += sum(problem)
            else:
                problem.append(int(instructions[idx][col_idx]))
    return total


def solve2(problem: tuple[str]) -> int:
    normal_numbers = problem[:-1]
    operator = problem[-1][0]
    celo_numbers = list(zip(*normal_numbers))
    operands = []
    for num in celo_numbers:
        hold = "".join(num)
        try:
            operands.append(int(hold.strip()))
        except ValueError:
            continue

    if operator == "*":
        return prod(operands)
    else:
        return sum(operands)


def main() -> None:
    here = Path(__file__).parent
    file_name = here / "input"
    # file_name = here / "test"
    operator_indices, lines = read_file(file_name)
    problems = []
    print(operator_indices, lines)
    for line in lines:
        problem = []
        for idx, op_idx in enumerate(operator_indices):
            if idx == len(operator_indices) - 1:
                problem.append(line[op_idx:])
            else:
                problem.append(line[op_idx:operator_indices[idx+1]])
        problems.append(problem)
    transposed = list(zip(*problems))
    total = sum(solve2(item) for item in transposed)
    print(total)


if __name__ == "__main__":
    main()
