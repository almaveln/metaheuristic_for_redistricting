"""
Generates a custom case along with the most optimal solution for it

One district is a 3x3 case

Output: two json files. One contains "raw" data for a generated region
and the other one contains the most optimal solution for it
"""
import json
import math
import collections

OPTIMAL_SLN_FILE_NAME = "region_30_30_opt_sln.json"
REGION_DATA_FILE_NAME = "region_30_30_data.json"
REP_SUPPORT_IN_3_BY_3_LAYOUT = [[0.6, 0.4, 0.7],
                                [0.5, 0.5, 0.3],
                                [0.3, 0.8, 0.4]]
NROWS = 30
NCOLUMNS = 30

TAKE_DOUBLE = True
NUMBER_OF_DISTRICTS = int(NROWS * NCOLUMNS / 36)
DISTRICTS = [[] for _ in range(NUMBER_OF_DISTRICTS)]
NUMBER_OF_DISTRICTS_IN_ROW = int(NCOLUMNS / 6)
NUMBER_OF_DISTRICTS_IN_COLUMN = int(NROWS / 6)


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


def is_on_region_border(unit_index: int, rows: int, columns: int):
    """Checks if unit_index is located on the region border"""

    assert rows * columns >= unit_index > 0
    unit_row_index = math.ceil(unit_index / rows)
    unit_column_index = unit_index % columns if unit_index % columns != 0 else columns

    # first row, last row, first column, last column
    return (unit_row_index == 1 or unit_row_index == rows or
            unit_column_index == 1 or unit_column_index == columns)


def select_republican_support(support, unit_index: int, nrows: int, ncolumns: int):
    """Selects the right percentage from support"""

    unit_row_index = math.ceil(unit_index / nrows)
    unit_column_index = unit_index % ncolumns if unit_index % ncolumns != 0 else ncolumns

    support_row_index = unit_row_index % 3 - 1 if unit_row_index % 3 != 0 else 2
    support_column_index = unit_column_index % 3 - 1 if unit_column_index % 3 != 0 else 2
    return support[support_row_index][support_column_index]


def get_dist_number_by_unit_number(unit_number, nrows, ncolumns):
    """Returns a district number to which the unit number belongs"""

    # print("dists {0}, unit_index {1}, nrows {2}, ncolumns {3}".format(dists, unit_index, nrows, ncolumns))
    Cell = collections.namedtuple("Cell", "row_index, column_index")
    cell_row_index = int(math.ceil(unit_number / nrows))
    cell_column_index = unit_number % ncolumns if unit_number % ncolumns != 0 else ncolumns
    _cell = Cell(cell_row_index, cell_column_index)

    multiplier = int((_cell.row_index - 1) / 6)
    district_numbers_in_this_row = [i + (multiplier * NUMBER_OF_DISTRICTS_IN_ROW)
                                    for i in range(1, NUMBER_OF_DISTRICTS_IN_ROW + 1)]

    # print(district_numbers_in_this_row)
    # print(unit_row_index)
    index_of_district_in_this_row = int((_cell.column_index - 1) / 6)
    # print(index_of_district_in_this_row)
    dist_number = district_numbers_in_this_row[index_of_district_in_this_row]
    return dist_number


def generate_region_data(nrows: int, ncolumns: int):
    assert nrows == ncolumns and nrows % 3 == 0 and ncolumns % 3 == 0
    obj = {}
    pop = 100

    obj["rows"] = nrows
    obj["columns"] = ncolumns
    obj["units"] = []

    for unit_number in range(1, nrows * ncolumns + 1):
        unit_obj = {}
        unit_obj["id"] = unit_number
        unit_obj["neighbors"] = get_neighbors(unit_number, nrows, ncolumns)
        unit_obj["is_on_region_border"] = is_on_region_border(unit_number, nrows, ncolumns)
        unit_obj["pop"] = pop
        unit_obj["registration"] = {}
        unit_obj["registration"]["rep"] = select_republican_support(REP_SUPPORT_IN_3_BY_3_LAYOUT, unit_number, nrows,
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
