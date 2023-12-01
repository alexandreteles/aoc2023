import os

with open(os.path.join(os.path.dirname(__file__), "input"), "r") as f:
    data = f.read().splitlines()


def get_first_and_last_digits(code: str) -> int:
    first_digit = None
    last_digit = None

    for char in code:
        if char.isdigit():
            first_digit = char
            break
    for char in reversed(code):
        if char.isdigit():
            last_digit = char
            break

    return int(first_digit + last_digit)


total = sum(list(map(get_first_and_last_digits, data)))

print(total)
