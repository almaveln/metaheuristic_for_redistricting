"""A visualisation tool for generated solutions"""

import json

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import pandas
from matplotlib.table import Table

# https://graphicdesign.stackexchange.com/questions/3682/where-can-i-find-a-large-palette-set-of-contrasting-colors-for-coloring-many-d
# COLORS = ["#d7191c", "#fdae61", "#ffffbf", "#abdda4", "#2b83ba"]
# TODO: images are cut off
# TODO: add a quality score to some place
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

# colors_contrast = ['#F2F3F4', '#F3C300', '#875692', '#F38400', '#A1CAF1',
#                    '#BE0032', '#C2B280', '#848482', '#008856', '#E68FAC', '#0067A5',
#                    '#F99379', '#604E97', '#F6A600',
#                    '#B3446C', '#DCD300', '#882D17', '#8DB600', '#654522', '#E25822']


def main():
    # output_path = "../output/output_2018-03-01_23:17:01.csv"
    # output_path = "../output_sa/output_test_2018-03-26_22:07:09.csv"
    output_path = "../output_sa/output_test_2018-04-08_21:08:46.csv"
    # data_path = "../data/data_3_3.json"
    data_path = "../data/data_3_3_rook_adj.json"
    title = "3x3 simple case"
    # img_path = "../visualisation_output/simple_case_3_3.png"
    img_path = "../visualisation_output_sa/simple_case_3_3_{0}.png"
    for i in [5000]:
        new_img_path = img_path.format(i)
        visualize_iteration(output_path, data_path, title, new_img_path, i)


def run_visualiser(input_file, data_file, img_output_file, title="Simple case"):
    output = pandas.read_csv(input_file, sep="|")
    df = pandas.DataFrame(output)
    iterations = len(df)
    print(iterations)
    for i in range(iterations):
        new_output_file = img_output_file.format(i)
        visualize_iteration(input_file, data_file, title, new_output_file, i)


def visualise_iterations(input_file, data_file, img_output_file, start, stop, title="Simple case"):
    output = pandas.read_csv(input_file, sep="|")
    for i in range(start, stop + 1):
        new_output_file = img_output_file.format(i)
        visualize_iteration(input_file, data_file, title, new_output_file, i)


def visualize_iteration(output_path, data_path, title, img_path, iteration=1):
    output = pandas.read_csv(output_path, sep="|")
    df = pandas.DataFrame(output)
    row = df[df['iteration'] == iteration]
    region_series = row["elite_solution_structure"]
    quality_score = row["sln_quality"]
    print(quality_score)
    region_json_str = region_series.iloc[0]

    data = pandas.read_json(data_path)
    fig, ax1 = plt.subplots()

    # title = title + "; quality score: {0}".format(quality_score.iloc[0])
    checkerboard_table(ax1, data, region_json_str)

    # plt.title(title, y=1.06, fontsize=26)
    # plt.title(title)
    # plt.tight_layout(pad=2, w_pad=0, h_pad=4.0)
    # plt.gcf().subplots_adjust(left=0.06, right=0.95, bottom=0.1, top=0.95)
    plt.gcf().subplots_adjust(left=0.06, right=0.95, bottom=0.35, top=0.95)
    plt.savefig(img_path, dpi=100)


def find_district_id_by_unit_id(region, unit_id):
    for district in region:
        if unit_id in district["units_ids"]:
            return district["district_id"]
    raise AssertionError("unit_id was not found in any district")


def get_color_patches(colors):
    patches = []
    for i, color in enumerate(colors):
        patches.append(mpatches.Patch(color=color, label='District ' + str(i + 1)))
    return patches


def checkerboard_table(ax, data, region_json_str, fmt='{:.2f}'):
    loaded_region = json.loads(region_json_str)
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
        tb.add_cell(row_index, column_index, width, height,
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

    color_patches = get_color_patches(colors)
    ax.legend(handles=color_patches, loc='upper center', bbox_to_anchor=(0.5, 0),
              shadow=True, ncol=4)


def visualize_parallel_sa_region_18_initial_maps():
    TEST_ID_NUMBER = 50
    REGION_ID = "region_18_18"
    TEST_SUITE_ID = "test_suite_2"
    SA_VERSION = "parallel"
    REGION_DATA_FILE_PATH_18_18 = "../data/{0}/{0}_data.json".format(REGION_ID)
    OUTPUT_FILE_18_18 = ("../experiments_output/{0}/{1}/{2}/"
                         "output_{2}_sa_v1_run_{3}_rank{4}.csv"
                         .format(SA_VERSION, TEST_SUITE_ID, REGION_ID, TEST_ID_NUMBER, 0))

    title_18_18 = "Region 18x18"
    IMG_OUTPUT_TEMPLATE_18_18 = ("../visualisation_output_sa/{0}/{1}/{2}/"
                                 "out_img_{2}_sa_v1_run_{3}_rank{4}_iter{5}.png"
                                 .format(SA_VERSION, TEST_SUITE_ID, REGION_ID, TEST_ID_NUMBER, 0, 0))

    import os

    print(os.path.isfile(OUTPUT_FILE_18_18))

    visualise_iterations(OUTPUT_FILE_18_18,
                         REGION_DATA_FILE_PATH_18_18,
                         IMG_OUTPUT_TEMPLATE_18_18, 0, 0)

    for rank in range(0, 60):
        OUTPUT_FILE_18_18 = ("../experiments_output/{0}/{1}/{2}/"
                             "output_{2}_sa_v1_run_{3}_rank{4}.csv"
                             .format(SA_VERSION, TEST_SUITE_ID, REGION_ID, TEST_ID_NUMBER, rank))
        IMG_OUTPUT_TEMPLATE_18_18 = ("../visualisation_output_sa/{0}/{1}/{2}/"
                                     "out_img_{2}_sa_v1_run_{3}_rank{4}_iter{5}.png"
                                     .format(SA_VERSION, TEST_SUITE_ID, REGION_ID, TEST_ID_NUMBER, rank, 0))

        visualise_iterations(OUTPUT_FILE_18_18,
                             REGION_DATA_FILE_PATH_18_18,
                             IMG_OUTPUT_TEMPLATE_18_18, 0, 0, "Instance " + str(rank))


def visualize_sequential_sa_test_suite_1_region_16_best_sln():
    # best_quality
    TEST_ID_NUMBER = 20
    REGION_ID = "region_16_16"
    TEST_SUITE_ID = "test_suite_1"
    SA_VERSION = "sequential"
    REGION_DATA_FILE_PATH_16_16 = "../data/{0}/{0}_data.json".format(REGION_ID)
    OUTPUT_FILE_16_16 = ("../experiments_output/{0}/{1}/{2}_seq/"
                         "output_{2}_sa_v1_run_{3}_seq.csv"
                         .format(SA_VERSION, TEST_SUITE_ID, REGION_ID, TEST_ID_NUMBER))

    title_18_18 = "Region 16x16"
    IMG_OUTPUT_TEMPLATE_16_16 = ("../visualisation_output_sa/{0}/{1}/{2}/"
                                 "out_img_{2}_sa_v1_run_{3}_best_sln.png"
                                 .format(SA_VERSION, TEST_SUITE_ID, REGION_ID, TEST_ID_NUMBER))

    import os

    print(os.path.isfile(OUTPUT_FILE_16_16))

    visualise_iterations(OUTPUT_FILE_16_16,
                         REGION_DATA_FILE_PATH_16_16,
                         IMG_OUTPUT_TEMPLATE_16_16, 5000, 5000)


def visualize_sequential_sa_test_suite_2_region_30_best_sln():
    # sln_quality
    TEST_ID_NUMBER = 1
    REGION_ID = "region_30_30"
    TEST_SUITE_ID = "test_suite_2"
    SA_VERSION = "sequential"
    REGION_DATA_FILE_PATH_30_30 = "../data/{0}/{0}_data.json".format(REGION_ID)
    OUTPUT_FILE_30_30 = ("../experiments_output/{0}/{1}/{2}/"
                         "output_{2}_sa_v1_id{3}.csv"
                         .format(SA_VERSION, TEST_SUITE_ID, REGION_ID, TEST_ID_NUMBER))

    title_18_18 = "Region 16x16"
    IMG_OUTPUT_TEMPLATE_30_30 = ("../visualisation_output_sa/{0}/{1}/{2}/"
                                 "out_img_{2}_sa_v1_id_{3}_best_sln.png"
                                 .format(SA_VERSION, TEST_SUITE_ID, REGION_ID, TEST_ID_NUMBER))

    import os
    print(os.path.isfile(OUTPUT_FILE_30_30))

    visualise_iterations(OUTPUT_FILE_30_30,
                         REGION_DATA_FILE_PATH_30_30,
                         IMG_OUTPUT_TEMPLATE_30_30, 5000, 5000)


if __name__ == "__main__":
    # main()
    # DATA_FILE_6_6 = "../utils/test.json"
    # OUTPUT_FILE_6_6 = "../output_sa/output_test_6_6_picked.csv"
    # IMG_OUTPUT_TEMPLATE_6_6 = "../visualisation_output_sa/simple_case_6_6_picked_{0}.svg"
    # visualise_iterations(OUTPUT_FILE_6_6, DATA_FILE_6_6, IMG_OUTPUT_TEMPLATE_6_6, 5000, 5000)

    # TEST_ID_NUMBER = 1
    # REGION_DATA_FILE_PATH_24_24 = "../data/region_24_24/region_24_24_data.json"
    # title_24_24 = "Region 24x24"
    # img_path_24_24 = "../visualisation_output_sa/region_24_24/region_24_24_opt_sln_vis.svg"
    # IMG_OUTPUT_TEMPLATE_24_24 = "../visualisation_output_sa/region_24_24/out_img_region_24_24_sa_v1_id{0}_iter{1}.png".format(
    #     TEST_ID_NUMBER, "{0}")
    # OUTPUT_FILE_24_24 = "../experiments_output/region_24_24/output_region_24_24_sa_v1_id1.csv"
    # PLOT_FILE_24_24 = "../plotting_output/region_24_24/plot_{1}_region_24_24_sa_v1_id{0}.png".format(TEST_ID_NUMBER,
    #                                                                                                  "{0}")
    # analyse(OUTPUT_FILE_24_24, PLOT_FILE_24_24.format("energy"), "iteration", "current_energy", "iteration",
    #                  "current_energy")
    # analyse(OUTPUT_FILE_24_24, PLOT_FILE_24_24.format("time"), "iteration", "cumtime", "iteration", "cumtime")
    # visualise_iterations(OUTPUT_FILE_24_24, REGION_DATA_FILE_PATH_24_24, IMG_OUTPUT_TEMPLATE_24_24, 5000,
    #                      5000)
    # visualize_parallel_sa_region_18_initial_maps()
    # visualize_sequential_sa_test_suite_1_region_16_best_sln()
    visualize_sequential_sa_test_suite_2_region_30_best_sln()
