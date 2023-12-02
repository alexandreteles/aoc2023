import os

# A dictionary representing a bag containing a certain number of colored items.
BAG: dict[str, int] = {"red": 12, "green": 13, "blue": 14}


def get_game_number(game_line: str) -> int:
    """
    Extracts and returns the game number from a string.

    Args:
    game_line (str): A string representing a game, e.g., "Game 1: ..."

    Returns:
    int: The game number.
    """
    # Extract the game number from a game line.
    return int(game_line.split(" ")[1].strip(":"))


def get_game_scores(game_line: str) -> list[int]:
    """
    Splits a game line into individual round outcomes.

    Args:
    game_line (str): A string representing the outcomes of a game's rounds.

    Returns:
    list[int]: A list of strings, each representing the outcome of a round.
    """
    # Split a game line into individual round outcomes.
    return [pull.strip() for pull in game_line.split(":")[1].split(";")]


def convert_pulls_to_dict(pulls: list[str]) -> dict[str, int]:
    """
    Converts a list of strings representing pulls into a list of dictionaries.

    Args:
    pulls (list[str]): A list of strings, each representing a pull of items.

    Returns:
    list[dict[str, int]]: A list of dictionaries with colors as keys and counts as values.
    """
    # Convert the string representation of pulls into a list of dictionaries.
    return [
        dict(
            map(
                lambda kv: (kv[1], int(kv[0])),  # Convert "10 green" to {"green": 10}
                [
                    pair.split() for pair in item.split(",")
                ],  # Split each pull into color and amount.
            )
        )
        for item in pulls
    ]


def check_valid_game(pulls: list[dict[str, int]]) -> bool:
    """
    Checks if the pulls in a game are valid based on the BAG constraints.

    Args:
    pulls (list[dict[str, int]]): A list of dictionaries representing the pulls in a game.

    Returns:
    bool: True if all pulls are valid, False otherwise.
    """
    # Check if all the pulls in a game are valid based on the available counts in BAG.
    return all(
        amount <= BAG[color]  # Ensure each pull does not exceed the available count.
        for item_dict in pulls
        for color, amount in item_dict.items()
    )


def helper(game: str) -> int:
    """
    Helper function to process each game line and validate it.

    Args:
    game (str): A string representing a game.

    Returns:
    int: The game number if the game is valid, 0 otherwise.
    """
    # Process each game line: check its validity and return its number if valid.
    if check_valid_game(convert_pulls_to_dict(get_game_scores(game))):
        return get_game_number(game)
    else:
        return 0


# Reading input data from a file in the same directory as the script.
with open(os.path.join(os.path.dirname(__file__), "input"), "r") as file:
    input_data: list[str] = file.read().splitlines()

# Calculating the sum of valid game numbers from the input data.
part_1: int = sum(list(filter(lambda x: x != 0, map(helper, input_data))))
print(f"Part 1: {part_1}")
