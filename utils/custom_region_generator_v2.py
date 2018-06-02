"""
Generates a custom case along with the most optimal solution for it

One district is a 3x3 case

Output: two json files. One contains "raw" data for a generated region
and the other one contains the most optimal solution for it
"""
import json
import math

NROWS = 4
NCOLUMNS = 4

OPTIMAL_SLN_FILE_NAME = "region_{0}_{1}_opt_sln.json".format(NROWS, NCOLUMNS)
REGION_DATA_FILE_NAME = "region_{0}_{1}_data.json".format(NROWS, NCOLUMNS)


NUMBER_OF_DISTRICTS = 4
DISTRICTS = [[] for _ in range(NUMBER_OF_DISTRICTS)]
NUMBER_OF_DISTRICTS_IN_ROW = 2
NUMBER_OF_DISTRICTS_IN_COLUMN = 2


def generate_district_layout(nrows, ncolumns):
    # print(int(nrows * ncolumns / NUMBER_OF_DISTRICTS))

    # rep_percent = [0.7, 0.4, 0.3, 0.8, 0.3]
    add_column = [0.7, 0.4, 0.3, 0.5, 0.8, 0.4, 0.5]
    add_row = [0.3, 0.8, 0.3, 0.7, 0.5, 0.2, 0.6, 0.5]

    layout_options = [4, 6, 8, 10, 12, 14, 16]

    support_2 = [[0.7, 0.4],
                 [0.6, 0.3]]

    support = support_2

    order_number = layout_options.index(nrows)

    for i in range(order_number):
        for j, row in enumerate(support):
            row.append(add_column[j])
        support.append(add_row[:(i + 3)])

    # for row in support:
    #     print(row)

    return support


def is_on_region_border(unit_index: int, rows: int, columns: int):
    """Checks if unit_index is located on the region border"""

    assert rows * columns >= unit_index > 0
    unit_row_index = math.ceil(unit_index / rows)
    unit_column_index = unit_index % columns if unit_index % columns != 0 else columns

    # first row, last row, first column, last column
    return (unit_row_index == 1 or unit_row_index == rows or
            unit_column_index == 1 or unit_column_index == columns)


def get_neighbors(unit_index: int, rows: int, columns: int):
    """Get neighbors of unit_index. 8 is the maximum number of possible neighbors"""

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


def select_republican_support(support, unit_index: int, nrows: int, ncolumns: int):
    """Selects the right percentage from support"""

    unit_row_index = math.ceil(unit_index / nrows)
    unit_column_index = unit_index % ncolumns if unit_index % ncolumns != 0 else ncolumns

    half_rows = int(nrows / 2)
    half_columns = int(nrows / 2)

    first_index = unit_row_index if unit_row_index <= half_rows else unit_row_index - half_rows
    second_index = unit_column_index if unit_column_index <= half_columns else unit_column_index - half_columns

    # print("first_index {0}, row_index {1}".format(first_index, unit_row_index))
    # print("second_index {0}, column_index {1}".format(second_index, unit_column_index))
    # print("support {0}".format(support[first_index - 1][second_index - 1]))
    return support[first_index - 1][second_index - 1]


def get_dist_number_by_unit_number(unit_number, nrows, ncolumns):
    """Returns a district number to which the unit number belongs"""

    districts_numbers = [[1, 2], [3, 4]]

    half_rows = int(nrows / 2)
    half_columns = int(nrows / 2)

    cell_row_index = int(math.ceil(unit_number / nrows))
    cell_column_index = unit_number % ncolumns if unit_number % ncolumns != 0 else ncolumns
    first_index = 0 if cell_row_index <= half_rows else 1
    second_index = 0 if cell_column_index <= half_columns else 1
    return districts_numbers[first_index][second_index]


def generate_region_data(nrows: int, ncolumns: int):
    assert nrows == ncolumns and nrows % 2 == 0 and ncolumns % 2 == 0
    obj = {}
    pop = 100

    obj["rows"] = nrows
    obj["columns"] = ncolumns
    obj["units"] = []

    support = generate_district_layout(nrows, ncolumns)
    for unit_number in range(1, nrows * ncolumns + 1):
        unit_obj = {}
        unit_obj["id"] = unit_number
        unit_obj["neighbors"] = get_neighbors(unit_number, nrows, ncolumns)
        unit_obj["is_on_region_border"] = is_on_region_border(unit_number, nrows, ncolumns)
        unit_obj["pop"] = pop
        unit_obj["registration"] = {}
        unit_obj["registration"]["rep"] = select_republican_support(support, unit_number, nrows,
                                                                    ncolumns)
        unit_obj["registration"]["dem"] = round(1 - unit_obj["registration"]["rep"], 2)
        obj["units"].append(unit_obj)
        dist_number = get_dist_number_by_unit_number(unit_number, nrows, ncolumns)
        DISTRICTS[dist_number - 1].append(unit_number)

    with open(REGION_DATA_FILE_NAME, "w") as file:
        json.dump(obj, file)

    return DISTRICTS


def generate_optimal_sln_data(dists):
    result = []
    for i, el in enumerate(dists):
        result.append({'district_id': i + 1, 'units_ids': el})

    with open(OPTIMAL_SLN_FILE_NAME, "w") as file:
        json.dump({"result": result}, file)


def run_region_generator():
    dists = generate_region_data(NROWS, NCOLUMNS)
    generate_optimal_sln_data(dists)


if __name__ == "__main__":
    run_region_generator()

    # nrows = 8
    # ncolumns = 8
    # support = generate_district_layout(nrows, ncolumns)
    # print(support)