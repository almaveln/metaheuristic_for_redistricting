"""A visualisation tool for visualising optimal regions (solutions)"""

import json

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import pandas
from matplotlib.table import Table

# https://graphicdesign.stackexchange.com/questions/3682/where-can-i-find-a-large-palette-set-of-contrasting-colors-for-coloring-many-d
# COLORS = ["#d7191c", "#fdae61", "#ffffbf", "#abdda4", "#2b83ba"]
# TODO: images are cut off
# TODO: add a quality score to some place
# TODO: find distinct slick colors for districts up to 20 (?)

COLORS = ["#FFFF00", "#1CE6FF", "#006FA6", "#A30059", "#6B7900", "#00C2A0", "#FFAA92",
          "#FF34FF", "#997D87", "#7A4900", "#D16100", "#FF4A46", "#B903AA", "#B4A8BD" ,
          "#FF90C9", "#FFDBE5", "#BEC459", "#63FFAC", "#B79762", "#8FB0FF", "#DDEFFF",
          "#809693", "#FEFFE6", "#A3C8C9", "#3B5DFF", "#4FC601", "#4A3B53", "#7900D7",
          "#61615A", "#BA0900", "#6B7900", "#00C2A0", "#BA0900", "#61615A", "#FFAA92",
          "#FF90C9", "#D16100", "#7B4F4B", "#A1C299", "#0AA6D8", "#00846F", "#C2FFED",
          "#A079BF", "#CC0744", "#C0B9B2", "#C2FF99", "#00489C", "#6F0062", "#0CBD66",
          "#EEC3FF", "#456D75", "#B77B68", "#7A87A1", "#788D66", "#885578", "#FAD09F",
          "#FF8A9A", "#D157A0", "#456648", "#0086ED", "#886F4C", "#34362D", "#FFB500",
          "#00A6AA", "#452C2C", "#636375", "#FF913F", "#938A81", "#575329", "#00FECF",
          "#B05B6F", "#8CD0FF", "#3B9700", "#04F757", "#C8A1A1", "#1E6E00", "#A77500",
          "#6367A9", "#A05837", "#6B002C", "#772600", "#D790FF", "#9B9700", "#549E79",
          "#FFF69F", "#72418F", "#BC23FF", "#99ADC0", "#3A2465", "#922329", "#5B4534",
          "#FDE8DC", "#404E55", "#0089A3", "#CB7E98", "#A4E804", "#324E72", "#6A3A4C"]


def main():
    opt_sln_path = "../data/region_6_6/region_6_6_opt_sln_ts2.json"
    region_data_path = "../data/region_6_6/region_6_6_data_ts2.json"
    title = "Region 3x3"
    img_path = "../visualisation_output_sa/region_6_6/region_6_6_opt_sln_vis_test.svg"
    visualize_iteration(opt_sln_path, region_data_path, title, img_path)


def visualize_iteration(output_path, data_path, img_path):
    with open(output_path) as f:
        json_obj = json.load(f)
    region_json_str = json_obj
    region_json_str = region_json_str["result"]
    print(region_json_str)

    data = pandas.read_json(data_path)
    fig, ax1 = plt.subplots()

    checkerboard_table(ax1, data, region_json_str)

    # plt.tight_layout(pad=2, w_pad=0, h_pad=4.0)
    plt.gcf().subplots_adjust(left=0.06,right=0.95,bottom=0.35,top=0.95)
    # plt.gcf().subplots_adjust(bottom=0.12)
    plt.savefig(img_path, dpi=100)


def find_district_id_by_unit_id(region, unit_id):
    for district in region:
        if unit_id in district["units_ids"]:
            return district["district_id"]
    raise KeyError


def get_color_patches(colors):
    patches = []
    for i, color in enumerate(colors):
        patches.append(mpatches.Patch(color=color, label='District ' + str(i + 1)))
    return patches


def checkerboard_table(ax, data, region_json_str, fmt='{:.2f}'):
    loaded_region = region_json_str
    nrows = data["rows"][0]
    ncolumns = data["columns"][0]
    ax.set_axis_off()
    tb = Table(ax, bbox=[0, 0, 1, 1])
    colors = COLORS[:len(loaded_region)]
    width, height = 1.0 / ncolumns, 1.0 / nrows

    # Add cells
    row_index = 1
    for _, unit_data in enumerate(data["units"]):
        id_val = unit_data["id"]
        rep = unit_data["registration"]["rep"]
        column_index = id_val % ncolumns
        column_index = column_index if column_index != 0 else ncolumns

        color_id = find_district_id_by_unit_id(loaded_region, id_val)
        color = colors[color_id - 1]

        # facecolor - background color
        tb.add_cell(row_index, column_index, width, height, text=fmt.format(rep),
                    loc='center', facecolor=color)

        if column_index == ncolumns:
            row_index += 1

    # Row Labels...
    for i in range(1, nrows + 1):
        tb.add_cell(i, -1, width, height, text=i, loc='right',
                    edgecolor='none', facecolor='none')
    # Column Labels...
    for j in range(1, ncolumns + 1):
        tb.add_cell(-1, j, width, height / 2, text=j, loc='center',
                    edgecolor='none', facecolor='none')

    tb.set_fontsize(16)
    ax.add_table(tb)

    color_patches = get_color_patches(colors)
    ax.legend(handles=color_patches, loc='upper center', bbox_to_anchor=(0.5, 0), shadow=True,
              ncol=4)


def visualize_data_test_suite_y_region_x(test_suite_y, region_x):
    REGION_DATA_FILE_PATH = "../data/{0}/{0}_data.json".format(region_x)
    OPTIMAL_SLN_FILE_PATH = "../data/{0}/{0}_opt_sln.json".format(region_x)
    IMG_OUTPUT_TEMPLATE = ("../visualisation_output_sa/data/{0}/{1}/"
                           "optimal_sln_{0}_{1}.png"
                           .format(test_suite_y, region_x))

    visualize_iteration(OPTIMAL_SLN_FILE_PATH, REGION_DATA_FILE_PATH,
                        IMG_OUTPUT_TEMPLATE)


if __name__ == "__main__":
    pass
    # OPTIMAL_SLN_FILE_PATH_3_3 = "../data/region_3_3/region_3_3_opt_sln.json"
    # REGION_DATA_FILE_PATH_3_3 = "../data/region_3_3/region_3_3_data.json"
    # title_3_3 = "Region 3x3"
    # img_path_3_3 = "../visualisation_output_sa/region_3_3/region_3_3_opt_sln_vis.svg"
    # visualize_iteration(OPTIMAL_SLN_FILE_PATH_3_3, REGION_DATA_FILE_PATH_3_3, title_3_3, img_path_3_3)

    # OPTIMAL_SLN_FILE_PATH_6_6 = "../data/region_6_6/region_6_6_opt_sln_ts2.json"
    # REGION_DATA_FILE_PATH_6_6 = "../data/region_6_6/region_6_6_data_ts2.json"
    # title_6_6 = "Region 6x6"
    # img_path_6_6 = "../visualisation_output_sa/region_6_6/region_6_6_opt_sln_vis_v1.svg"
    # visualize_iteration(OPTIMAL_SLN_FILE_PATH_6_6, REGION_DATA_FILE_PATH_6_6, title_6_6, img_path_6_6)

    # OPTIMAL_SLN_FILE_PATH_18_18 = "../data/region_18_18/region_18_18_opt_sln.json"
    # REGION_DATA_FILE_PATH_18_18 = "../data/region_18_18/region_18_18_data.json"
    # title_18_18 = "Region 18x18"
    # img_path_18_18 = "../visualisation_output_sa/region_18_18/region_18_18_opt_sln_vis.svg"
    # visualize_iteration(OPTIMAL_SLN_FILE_PATH_18_18, REGION_DATA_FILE_PATH_18_18, title_18_18, img_path_18_18)
    #
    # OPTIMAL_SLN_FILE_PATH_24_24 = "../data/region_24_24/region_24_24_opt_sln.json"
    # REGION_DATA_FILE_PATH_24_24 = "../data/region_24_24/region_24_24_data.json"x
    # title_24_24 = "Region 24x24"
    # img_path_24_24 = "../visualisation_output_sa/region_24_24/region_24_24_opt_sln_vis.svg"
    # visualize_iteration(OPTIMAL_SLN_FILE_PATH_24_24, REGION_DATA_FILE_PATH_24_24, title_24_24, img_path_24_24)

    # OPTIMAL_SLN_FILE_PATH_30_30 = "../data/region_30_30/region_30_30_opt_sln.json"
    # REGION_DATA_FILE_PATH_30_30 = "../data/region_30_30/region_30_30_data.json"
    # title_30_30 = "Region 30x30"
    # img_path_30_30 = "../visualisation_output_sa/region_30_30/region_30_30_opt_sln_vis.svg"
    # visualize_iteration(OPTIMAL_SLN_FILE_PATH_30_30, REGION_DATA_FILE_PATH_30_30, title_30_30, img_path_30_30)

    # new test cases
    # OPTIMAL_SLN_FILE_PATH_4_4 = "../data/region_4_4/region_4_4_opt_sln.json"
    # REGION_DATA_FILE_PATH_4_4 = "../data/region_4_4/region_4_4_data.json"
    # title_4_4 = "Region 4x4"
    # img_path_4_4 = "../visualisation_output_sa/region_4_4/region_4_4_opt_sln_vis.png"
    # visualize_iteration(OPTIMAL_SLN_FILE_PATH_4_4, REGION_DATA_FILE_PATH_4_4, title_4_4, img_path_4_4)

    # OPTIMAL_SLN_FILE_PATH_6_6 = "../data/region_6_6/region_6_6_opt_sln.json"
    # REGION_DATA_FILE_PATH_6_6 = "../data/region_6_6/region_6_6_data.json"
    # title_6_6 = "Region 6_6"
    # img_path_6_6 = "../visualisation_output_sa/region_6_6/region_6_6_opt_sln_vis.png"
    # visualize_iteration(OPTIMAL_SLN_FILE_PATH_6_6, REGION_DATA_FILE_PATH_6_6, title_6_6, img_path_6_6)
    #
    # OPTIMAL_SLN_FILE_PATH_8_8 = "../data/region_8_8/region_8_8_opt_sln.json"
    # REGION_DATA_FILE_PATH_8_8 = "../data/region_8_8/region_8_8_data.json"
    # title_8_8 = "Region 8x8"
    # img_path_8_8 = "../visualisation_output_sa/region_8_8/region_8_8_opt_sln_vis.png"
    # visualize_iteration(OPTIMAL_SLN_FILE_PATH_8_8, REGION_DATA_FILE_PATH_8_8, title_8_8, img_path_8_8)
    #
    # OPTIMAL_SLN_FILE_PATH_10_10 = "../data/region_10_10/region_10_10_opt_sln.json"
    # REGION_DATA_FILE_PATH_10_10 = "../data/region_10_10/region_10_10_data.json"
    # title_10_10 = "Region 10_10"
    # img_path_10_10 = "../visualisation_output_sa/region_10_10/region_10_10_opt_sln_vis.png"
    # visualize_iteration(OPTIMAL_SLN_FILE_PATH_10_10, REGION_DATA_FILE_PATH_10_10, title_10_10, img_path_10_10)
    #
    # OPTIMAL_SLN_FILE_PATH_12_12 = "../data/region_12_12/region_12_12_opt_sln.json"
    # REGION_DATA_FILE_PATH_12_12 = "../data/region_12_12/region_12_12_data.json"
    # title_12_12 = "Region 12_12"
    # img_path_12_12 = "../visualisation_output_sa/region_12_12/region_12_12_opt_sln_vis.png"
    # visualize_iteration(OPTIMAL_SLN_FILE_PATH_12_12, REGION_DATA_FILE_PATH_12_12, title_12_12, img_path_12_12)
    #
    # OPTIMAL_SLN_FILE_PATH_14_14 = "../data/region_14_14/region_14_14_opt_sln.json"
    # REGION_DATA_FILE_PATH_14_14 = "../data/region_14_14/region_14_14_data.json"
    # title_14_14 = "Region 14_14"
    # img_path_14_14 = "../visualisation_output_sa/region_14_14/region_14_14_opt_sln_vis.png"
    # visualize_iteration(OPTIMAL_SLN_FILE_PATH_14_14, REGION_DATA_FILE_PATH_14_14, title_14_14, img_path_14_14)
    #
    # OPTIMAL_SLN_FILE_PATH_16_16 = "../data/region_16_16/region_16_16_opt_sln.json"
    # REGION_DATA_FILE_PATH_16_16 = "../data/region_16_16/region_16_16_data.json"
    # title_16_16 = "Region 16_16"
    # img_path_16_16 = "../visualisation_output_sa/region_16_16/region_16_16_opt_sln_vis.png"
    # visualize_iteration(OPTIMAL_SLN_FILE_PATH_16_16, REGION_DATA_FILE_PATH_16_16, title_16_16, img_path_16_16)

    # visualize_data_test_suite_y_region_x("test_suite_1", "region_4_4")
    # visualize_data_test_suite_y_region_x("test_suite_1", "region_6_6")
    # visualize_data_test_suite_y_region_x("test_suite_1", "region_8_8")
    # visualize_data_test_suite_y_region_x("test_suite_1", "region_10_10")
    # visualize_data_test_suite_y_region_x("test_suite_1", "region_12_12")
    # visualize_data_test_suite_y_region_x("test_suite_1", "region_14_14")
    # visualize_data_test_suite_y_region_x("test_suite_1", "region_16_16")
    # visualize_data_test_suite_y_region_x("test_suite_1", "region_16_16")
    # visualize_data_test_suite_y_region_x("test_suite_2", "region_30_30")

    # visualize_data_test_suite_y_region_x("test_suite_2", "region_3_3")
    # visualize_data_test_suite_y_region_x("test_suite_2", "region_6_6")
    # visualize_data_test_suite_y_region_x("test_suite_2", "region_18_18")
    # visualize_data_test_suite_y_region_x("test_suite_2", "region_24_24")
    # visualize_data_test_suite_y_region_x("test_suite_2", "region_30_30")