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
    """
    Extracts the first and last digits from a string and concatenates them into an integer.

    Args:
    input_string (str): The string from which to extract digits.

    Returns:
    int: Concatenated integer of the first and last digit, or 0 if not found.
    """
    first_digit = next(
        (character for character in input_string if character.isdigit()), None
    )
    last_digit = next(
        (character for character in reversed(input_string) if character.isdigit()), None
    )

    if first_digit and last_digit:
        return int(first_digit + last_digit)
    else:
        return 0


def find_first_match_in_string(
    text_string: str, match_targets: list[str], search_backwards: bool = False
) -> Optional[int]:
    """
    Searches for the first occurrence of any target strings in a given text string.

    Args:
    text_string (str): The text to search through.
    match_targets (list[str]): Target strings to find in the text.
    search_backwards (bool, optional): If True, the search is performed in reverse. Defaults to False.

    Returns:
    Optional[int]: Index of the first matched target string, or None if no match is found.
    """
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
    """
    Processes a list of lines, searching for target strings and calculating a sum based on matching criteria.

    Args:
    target_strings (list[str]): Strings to match in each line.
    input_lines (list[str]): Lines of text to process.

    Returns:
    int: Sum of values derived from processing each line.
    """

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


# Read input file located in the same directory as this script.
with open(os.path.join(os.path.dirname(__file__), "input"), "r") as file:
    input_data: list[str] = file.read().splitlines()

# Print sum of first and last digits extracted from each line.
print(f"Step 1: {sum(list(map(extract_first_and_last_digits, input_data)))}")

# Print sum from processing lines with combined target strings and input data.
print(f"Step 2: {process_and_sum_lines(NUMERAL_STRINGS + WORD_DIGITS, input_data)}")
