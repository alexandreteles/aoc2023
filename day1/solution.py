import os
from typing import Optional

# Constants: lists for single-digit numerals and their textual representations.
NUMERAL_STRINGS: list[str] = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
WORD_DIGITS: list[str] = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def extract_first_and_last_digits(input_string: str) -> int:
    first_found_digit: Optional[str] = None
    last_found_digit: Optional[str] = None

    # Search for the first digit in the string.
    for character in input_string:
        if character.isdigit():
            first_found_digit = character
            break

    # Search for the last digit in the string, starting from the end.
    for character in reversed(input_string):
        if character.isdigit():
            last_found_digit = character
            break

    # Return concatenated digits as an integer, or 0 if not found.
    return (
        int(first_found_digit + last_found_digit)
        if first_found_digit and last_found_digit
        else 0
    )


def find_first_match_in_string(
    text_string: str, match_targets: list[str], search_backwards: bool = False
) -> Optional[int]:
    # Generate positions in the text to start the search, optionally in reverse.
    search_positions = (
        range(len(text_string))
        if not search_backwards
        else (-i - 1 for i in range(len(text_string)))
    )

    # Look for the first occurrence of any target string from each search position.
    match_finder = (
        (index % 9 + 1)
        for position in search_positions
        for index, target in enumerate(match_targets)
        if text_string[position:].startswith(target)
    )

    # Return the first match found, or None if no matches.
    return next(match_finder, None)


def process_and_sum_lines(target_strings: list[str], input_lines: list[str]) -> int:
    def calculate_line_value(current_line: str) -> int:
        # Search for matches in both forward and backward directions.
        match_forward = find_first_match_in_string(current_line, target_strings)
        match_backward = find_first_match_in_string(
            current_line, target_strings, search_backwards=True
        )

        # Calculate value based on matches, return 0 if any match is missing.
        return (
            (match_forward * 10 + match_backward)
            if match_forward and match_backward
            else 0
        )

    # Sum the calculated values for each line.
    return sum(map(calculate_line_value, input_lines))


if __name__ == "__main__":
    # Read input file located in the same directory as this script.
    with open(os.path.join(os.path.dirname(__file__), "input"), "r") as file:
        input_data: list[str] = file.read().splitlines()

    # Print sum of first and last digits extracted from each line.
    print(f"Step 1: {sum(list(map(extract_first_and_last_digits, input_data)))}")

    # Print sum from processing lines with combined target strings and input data.
    print(f"Step 2: {process_and_sum_lines(NUMERAL_STRINGS + WORD_DIGITS, input_data)}")
