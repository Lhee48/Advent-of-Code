from pathlib import Path
from AoC2025.Utils.utils import read_file


def downwards(lines: list[str]) -> int:
    n_splits = 0
    indices = set()
    for idx_row, row in enumerate(lines):
        for idx_col, col in enumerate(row):
            if col == "S":
                indices.add(idx_col)
            elif col == "^" and idx_col in indices:
                n_splits += 1
                indices.remove(idx_col)
                if idx_col - 1 > 0:
                    indices.add(idx_col - 1)
                if idx_col < len(row):
                    indices.add(idx_col + 1)
    return n_splits


def quantum_down(lines: list[str]) -> int:
    n_rows = len(lines)
    n_cols = len(lines[0])
    n_splits: list[list[int]] = [[0] * n_cols for _ in range(n_rows)]
    for idx_row, row in enumerate(lines):
        for idx_col, col in enumerate(row):
            if idx_row == len(lines) - 1: break
            if col == "S":
                n_splits[idx_row + 1][idx_col] = 1
            elif col == "^":
                n_splits[idx_row + 1][idx_col - 1] += n_splits[idx_row-1][idx_col]
                n_splits[idx_row + 1][idx_col + 1] += n_splits[idx_row-1][idx_col]
            elif idx_row != 0 and col == "." and lines[idx_row - 1][idx_col] != "S":
                n_splits[idx_row + 1][idx_col] += n_splits[idx_row-1][idx_col]
    return sum(n_splits[-1])


def main() -> None:
    here = Path(__file__).parent
    file_name = here / "input"
    # file_name = here / "test" 
    lines = read_file(file_name)
    part_1 = downwards(lines)
    part_2 = quantum_down(lines)
    print(part_1, part_2)


if __name__ == "__main__":
    main()
