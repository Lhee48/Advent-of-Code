from pathlib import Path
from AoC2025.Utils.utils import read_file


# Part 1 get the largest 2-digit number without rearranging
# def find_largest_joltage(bank: str) -> int:
#     largest_joltage_tens = 0
#     largest_joltage_ones = 1
#     for index, battery in enumerate(bank):
#         if battery > bank[largest_joltage_tens] and index != len(bank) - 1:
#             largest_joltage_tens = index
#             largest_joltage_ones = index + 1
#         if battery > bank[largest_joltage_ones] and index > largest_joltage_tens:
#             largest_joltage_ones = index
#     return int(bank[largest_joltage_tens] + bank[largest_joltage_ones])


# Part 2 get the largest 12-digit number without rearranging
def find_largest_joltage(bank: str) -> int:
    indices = [-1] * 12
    len_bank = len(bank)
    for i in range(12):
        start_idx = indices[i - 1] + 1 if i != 0 else 0
        print(bank[start_idx:len_bank-(11-i)])
        for idx, battery in enumerate(bank[start_idx:len_bank-(11-i)]):
            if indices[i] == -1 or int(battery) > int(bank[indices[i]]):
                indices[i] = start_idx + idx

            if battery == "9":
                break

    largest_digit = ""
    for idx in indices:
        largest_digit += bank[idx]
    print(indices, largest_digit)
    return int(largest_digit)


def main() -> None:
    here = Path(__file__).parent
    file_name = here / "input"
    # file_name = here / "test"
    banks = read_file(file_name)
    ans = sum(find_largest_joltage(bank) for bank in banks)
    print(ans)


if __name__ == "__main__":
    main()
