from utils import read_file


def count_target(instructions: list[str], right_limit = 100, target = 0, start = 50) -> int:
    # count how many times the counter lands on or passes through the target
    # e.g. R200 will pass around 0 twice
    counter = start
    answer = 0
    for instruction in instructions:
        direction = instruction[0].upper()

        try:
            value = int(instruction[1:])
        except ValueError:
            continue

        quotient, remainder = divmod(value, right_limit)
        answer += quotient

        previous = counter
        move = -remainder if direction == "L" else remainder
        counter += move

        if (counter < 0 and previous != 0) or counter > right_limit:
            answer += 1
        counter %= right_limit

        if counter == target:
            answer += 1
    return answer


def main() -> None:
    file_name = "input-1"
    # file_name = "test-1"
    instructions = read_file(file_name)
    ans = count_target(instructions)
    print(ans)


if __name__ == "__main__":
    main()
