"""
Contains tools that allow to visualise the political landscape of a region
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas
import matplotlib
from matplotlib.table import Table
import matplotlib.patches as mpatches


def visualise_json_input(in_file, out_file, title="Example title"):
    """Visualises the political landscape of a region"""

    data1 = pandas.read_json(in_file)
    fig, ax1 = plt.subplots()
    checkerboard_table(ax1, data1)

    # plt.tight_layout(pad=2, w_pad=0, h_pad=4.0)
    plt.gcf().subplots_adjust(bottom=0.12)
    plt.savefig(out_file, dpi=100)


def checkerboard_table(ax, data, fmt='{:.2f}'):
    BLUE = "#6475A6"
    RED = "#C02D16"
    nrows = data["rows"][0]
    ncolumns = data["columns"][0]
    ax.set_axis_off()
    tb = Table(ax, bbox=[0, 0, 1, 1])
    width, height = 1.0 / ncolumns, 1.0 / nrows

    # Add cells
    row_index = 1
    for _, unit_data in enumerate(data["units"]):
        color = "lightgray"
        id_val = unit_data["id"]
        rep = unit_data["registration"]["rep"]
        column_index = id_val % ncolumns
        column_index = column_index if column_index != 0 else ncolumns

        if rep < 0.5:
            color = BLUE

        if rep > 0.5:
            color = RED

        # facecolor - background color
        tb.add_cell(row_index, column_index, width, height, text=fmt.format(rep),
                    loc='center', facecolor=color)

        if column_index == ncolumns:
            row_index += 1

    # Row Labels...
    for i in range(1, nrows + 1):
        tb.add_cell(i, -1, width, height, text=i, loc='right', edgecolor='none',
                    facecolor='none')
    # Column Labels...
    for j in range(1, ncolumns + 1):
        tb.add_cell(-1, j, width, height / 2, text=j, loc='center', edgecolor='none',
                    facecolor='none')

    tb.set_fontsize(16)
    ax.add_table(tb)

    blue_patch = mpatches.Patch(color=BLUE, label='Democratic units')
    red_patch = mpatches.Patch(color=RED, label='Republican units')
    white_patch = mpatches.Patch(color='lightgray', label='Even support')
    ax.legend(handles=[red_patch, blue_patch, white_patch], loc='upper center',
              bbox_to_anchor=(0.5, 0), shadow=True, ncol=2)


def visualize_data_test_suite_y_region_x(region_x, test_suite_y):
    REGION_DATA_FILE_PATH = "../data/{0}/{0}_data.json".format(region_x)
    IMG_OUTPUT_TEMPLATE = ("../visualisation_output_sa/data/{0}/{1}/"
                           "out_politics_{0}_{1}.png"
                           .format(test_suite_y, region_x))
    visualise_json_input(REGION_DATA_FILE_PATH, IMG_OUTPUT_TEMPLATE)


if __name__ == '__main__':
    # visualize_data_test_suite_x_region_y("region_4_4", "test_suite_1")
    # visualize_data_test_suite_x_region_y("region_6_6", "test_suite_1")
    # visualize_data_test_suite_x_region_y("region_8_8", "test_suite_1")
    # visualize_data_test_suite_x_region_y("region_10_10", "test_suite_1")
    # visualize_data_test_suite_x_region_y("region_12_12", "test_suite_1")
    # visualize_data_test_suite_x_region_y("region_14_14", "test_suite_1")
    # visualize_data_test_suite_x_region_y("region_16_16", "test_suite_1")

    # visualize_data_test_suite_x_region_y("region_3_3", "test_suite_2")
    # visualize_data_test_suite_x_region_y("region_6_6", "test_suite_2")
    # visualize_data_test_suite_x_region_y("region_18_18", "test_suite_2")
    # visualize_data_test_suite_x_region_y("region_24_24", "test_suite_2")
    # visualize_data_test_suite_x_region_y("region_30_30", "test_suite_2")
    pass