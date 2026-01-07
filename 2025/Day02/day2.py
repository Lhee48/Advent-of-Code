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


# Part 1 Solution
# def add_invalid_ids(id_range: str) -> int:
#     """
#     Sums up invalid ids within the provided range
#     Invalid ids are sequence of digits repeated twice
#     e.g. 55, 6464, 123123
#     """
#     sum = 0
#     min_range, max_range = id_range.split('-')
#     digits_min = len(min_range)
#     digits_max = len(max_range)
#
#     # Both ranges are of the same number of digits and the number of digits are odd
#     if digits_min == digits_max and digits_min % 2 == 1:
#         return sum
#
#     # To be used to compare when either the min or the max range is odd
#     hold_min = min_range
#     hold_max = max_range
#
#     if digits_min % 2 == 1:
#         hold_min = "1" + ("0" * (digits_min))
#     if digits_max % 2 == 1:
#         hold_max = "9" * (digits_max - 1)
#
#     half_min_l = hold_min[0:len(hold_min)//2]
#     half_min_r = hold_min[len(hold_min)//2:]
#     half_max_l = hold_max[0:len(hold_max)//2]
#     half_max_r = hold_max[len(hold_max)//2:]
#
#     for index, i in enumerate(range(int(half_min_l), int(half_max_l) + 1)):
#         print(i)
#         if index == 0 and i < int(half_min_r):
#             continue
#         elif index == len(range(int(half_min_l), int(half_max_l) + 1)) - 1 and i > int(half_max_r):
#             continue
#         else:
#             sum += int(str(i)*2)
#     return sum

# Part 2 Solution
def add_invalid_ids(id_range: str) -> int:
    invalids = set()
    lo, hi = id_range.split('-')
    digits_lo = len(lo)
    digits_hi = len(hi)

    for digits in range(digits_lo, digits_hi + 1):
        for split in range(1, digits // 2 + 1):
            # We're only looking to split the digits evenly
            if digits % split != 0:
                continue

            multiplier = digits // split
            if multiplier < 2:
                continue

            # Generate invalid ids
            print(split, 10**(split-1), 10**split)
            for pattern in range(10 ** (split - 1), 10 ** split):
                invalid_id = int(str(pattern) * multiplier)

                if invalid_id > int(hi):
                    break
                if invalid_id >= int(lo):
                    invalids.add(invalid_id)

    return sum(invalids)

def main() -> None:
    # file_name = "day2-1"
    file_name = "test-2"
    product_ids = read_file(file_name)
    total = sum(add_invalid_ids(id_range) for id_range in product_ids)
    print(total)


if __name__ == "__main__":
    main()
