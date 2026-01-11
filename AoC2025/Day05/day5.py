from pathlib import Path


def read_file(file_name: Path) -> tuple[list[tuple[int, int]], list[int]]:
    path = Path(file_name)
    fresh: list[tuple[int, int]] = []
    ingredients: list[int] = []
    method = 1
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                if line.strip() == "":
                    method += 1
                elif method == 1:
                    id_range = line.split('-')
                    fresh.append((int(id_range[0]), int(id_range[1])))
                else:
                    ingredients.append(int(line.strip()))
        return (fresh, ingredients)
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: {path} nor found")


def main() -> None:
    here = Path(__file__).parent
    file_name = here / "input"
    # file_name = here / "test"

    n_fresh = 0
    fresh, ingredients = read_file(file_name)
    # Part 1
    for ingredient in ingredients:
        for lo, hi in fresh:
            if ingredient <= hi and ingredient >= lo:
                n_fresh += 1
                break
    print(n_fresh)

    # Part 2
    # How many ingredient IDs are considered to be fresh
    # according to the fresh ingredient ID ranges?
    fresh.sort()
    merged_ranges = []
    for lo, hi in fresh:
        if not merged_ranges or lo > merged_ranges[-1][1]:
            merged_ranges.append([lo, hi])
        else:
            merged_ranges[-1][1] = max(merged_ranges[-1][1], hi)
    unique_numbers = sum(end - start + 1 for start, end in merged_ranges)
    print(unique_numbers)


if __name__ == "__main__":
    main()
