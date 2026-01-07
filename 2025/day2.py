from pathlib import Path
import csv

def read_file(file_name: str) -> list[str]:
    path = Path(file_name)
    try:
        with open(path, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            return next(reader)
    except FileNotFoundError:
        print(f"Error: file '{file_name}' not found")
        return []


def main() -> None:
    file_name = "day2-1"
    product_ids = read_file(file_name)
    print(product_ids)


if __name__ == "__main__":
    main()
