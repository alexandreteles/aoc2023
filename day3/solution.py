import os
from math import prod
from functools import reduce


# Function to check if a character is a special symbol
def is_special(c):
    return c not in "0123456789."


# Function to get neighboring cells with special symbols
def get_neighboring_parts(i, j, data):
    return {
        (a, b)
        for a in range(max(i - 1, 0), min(i + 2, len(data)))
        for b in range(max(j - 1, 0), min(j + 2, len(data[i])))
        if is_special(data[a][b])
    }


# Function to process each cell
def process_cell(accumulator, grid_position_and_value):
    (total_numbers, special_symbols_parts, number, parts), (i, j, cell) = (
        accumulator,
        grid_position_and_value,
    )
    if cell.isdigit():
        number = number * 10 + int(cell)
        parts |= get_neighboring_parts(i, j, data_right_dot)
    else:
        if parts:
            total_numbers += number
            for part in parts:
                special_symbols_parts.setdefault(part, []).append(number)
        number, parts = 0, set()
    return (total_numbers, special_symbols_parts, number, parts)


if __name__ == "__main__":
    # Reading input data from a file in the same directory as the script.
    with open(os.path.join(os.path.dirname(__file__), "input"), "r") as file:
        data_right_dot: list[str] = [line + "." for line in file.read().splitlines()]

    # Flatten the grid and enumerate cells
    flat_grid = [
        (i, j, cell)
        for i, row in enumerate(data_right_dot)
        for j, cell in enumerate(row)
    ]

    # Use reduce to process the grid
    total_numbers, special_symbols_parts, _, _ = reduce(
        process_cell, flat_grid, (0, {}, 0, set())
    )

    # Calculate the product of pairs total
    product_of_pairs_total = sum(
        prod(special_symbols_parts[key])
        for key in special_symbols_parts
        if len(special_symbols_parts[key]) == 2
    )

    print(f"Part 1: {total_numbers}")
    print(f"Part 2: {product_of_pairs_total}")
