from pathlib import Path

def read_file(file_name: str) -> list[str]:
    path = Path(file_name)
    try:
        with open(path, "r", encoding="utf-8") as file:
            return [line.strip() for line in file if line.strip()] 
    except FileNotFoundError:
        print(f"Error: {path} not found")
        return []

