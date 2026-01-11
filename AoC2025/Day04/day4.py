from pathlib import Path


def read_file(file_name: Path) -> list[list[str]]:
    path = Path(file_name)
    try:
        with open(path, "r", encoding="utf-8") as file:
            return [list(line.strip()) for line in file if line.strip()] 
    except FileNotFoundError:
        print(f"Error: {path} not found")
        return []


def count_accessible(matrix: list[list[str]]) -> int:
    total = 0
    while True:
        old = total
        for n_row, row in enumerate(matrix):
            for n_col, col in enumerate(row):
                if col == ".":
                    continue
                adjacent = 0
                for change_row in [-1, 0, 1]:
                    for change_col in [-1,0,1]:
                        if (change_row == 0 and change_col == 0) or n_row + change_row < 0 or n_col + change_col < 0:
                            continue
                        try:
                            if matrix[n_row + change_row][n_col + change_col] == "@":
                                adjacent += 1
                        except IndexError:
                            continue
                if adjacent < 4:
                    matrix[n_row][n_col] = "."
                    total += 1
        if total - old == 0:
            break
    return total


def main() -> None:
    here = Path(__file__).parent
    file_name = here / "input"
    # file_name = here / "test"
    matrix = read_file(file_name)
    print(count_accessible(matrix))
    return


if __name__ == "__main__":
    main()
