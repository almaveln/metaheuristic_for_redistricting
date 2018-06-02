import json
import math
import random as rd


def get_neighbors(unit_index: int, rows: int, columns: int):
    """max neighbors 8"""
    assert rows * columns >= unit_index > 0

    max_possible_neighbors = 8
    neighbors = []

    unit_row_index = math.ceil(unit_index / rows)
    unit_column_index = unit_index % columns if unit_index % columns != 0 else columns
    for neighbor_index in range(1, max_possible_neighbors + 1):
        neighbor_id = 0

        if neighbor_index == 2:
            neighbor_id = unit_index - columns  # up
        elif neighbor_index == 4:
            # right
            neighbor_id = unit_index + 1 if unit_index + 1 <= unit_row_index * columns else 0
        elif neighbor_index == 6:
            neighbor_id = unit_index + columns  # down
        elif neighbor_index == 8:
            # left
            neighbor_id = unit_index - 1 if unit_index - 1 >= (unit_row_index - 1) * columns + 1 else 0

        if 0 < neighbor_id <= rows * columns:
            neighbors.append(neighbor_id)

    return sorted(neighbors)


def is_on_region_border(unit_index: int, rows: int, columns: int):
    assert rows * columns >= unit_index > 0
    unit_row_index = math.ceil(unit_index / rows)
    unit_column_index = unit_index % columns if unit_index % columns != 0 else columns

    # first row, last row, first column, last column
    if unit_row_index == 1 or unit_row_index == rows \
            or unit_column_index == 1 or unit_column_index == columns:
        return True

    return False


def generate_json_object(rows: int, columns: int):
    obj = {}
    pop = 100

    obj["rows"] = rows
    obj["columns"] = columns
    obj["units"] = []
    # rep_support = [0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7]
    # rep_support = [0.3, 0.4, 0.5, 0.6, 0.7]
    rep_support = [0.51, 0.49]
    for unit_index in range(1, rows * columns + 1):
        unit_obj = {}
        unit_obj["id"] = unit_index
        unit_obj["neighbors"] = get_neighbors(unit_index, rows, columns)
        unit_obj["is_on_region_border"] = is_on_region_border(unit_index, rows, columns)
        unit_obj["pop"] = pop
        unit_obj["registration"] = {}
        unit_obj["registration"]["rep"] = rd.choice(rep_support)
        unit_obj["registration"]["dem"] = round(1 - unit_obj["registration"]["rep"], 2)
        obj["units"].append(unit_obj)

    return obj


# print(get_neighbors(11, 4, 4))
# print(is_on_region_border(3, 4, 4))

if __name__ == "__main__":
    with open("data_30_30_rook_adj.json", "w") as file:
        json.dump(generate_json_object(30, 30), file)
