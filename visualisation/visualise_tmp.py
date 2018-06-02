import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import pandas
from matplotlib.table import Table

COLORS = ["#FFFF00", "#1CE6FF", "#FF34FF", "#FF4A46", "#B903AA", "#FFB500", "#006FA6", "#A30059",
          "#FFDBE5", "#7A4900", "#BEC459", "#63FFAC", "#B79762", "#8FB0FF", "#997D87",
          "#DDEFFF", "#809693", "#FEFFE6", "#A3C8C9", "#4FC601", "#3B5DFF", "#4A3B53", "#7900D7",
          "#61615A", "#BA0900", "#6B7900", "#00C2A0", "#FFAA92", "#FF90C9", "#D16100",
          "#7B4F4B", "#A1C299", "#0AA6D8", "#00846F", "#C2FFED", "#A079BF", "#CC0744", "#C0B9B2",
          "#C2FF99", "#00489C", "#6F0062", "#0CBD66", "#EEC3FF", "#456D75", "#B77B68", "#7A87A1", "#788D66",
          "#885578", "#FAD09F", "#FF8A9A", "#D157A0", "#456648", "#0086ED", "#886F4C",
          "#34362D", "#B4A8BD", "#00A6AA", "#452C2C", "#636375", "#FF913F", "#938A81",
          "#575329", "#00FECF", "#B05B6F", "#8CD0FF", "#3B9700", "#04F757", "#C8A1A1", "#1E6E00",
          "#A77500", "#6367A9", "#A05837", "#6B002C", "#772600", "#D790FF", "#9B9700",
          "#549E79", "#FFF69F", "#72418F", "#BC23FF", "#99ADC0", "#3A2465", "#922329",
          "#5B4534", "#FDE8DC", "#404E55", "#0089A3", "#CB7E98", "#A4E804", "#324E72", "#6A3A4C"]

region_example = [
    [42, 34, 43, 58, 35, 50],
    [19, 12, 38, 46, 21, 30, 23, 13, 22, 15, 20, 14],
    [17, 49, 9, 41, 33, 25, 57],
    [26, 27, 18],
    [10, 6, 2, 11, 4, 1, 3, 5, 7],
    [44, 29, 36, 28, 45, 37],
    [51, 61, 63, 53, 62, 55, 60, 54, 59, 52],
    [31, 24, 56, 64, 48, 16, 8, 47, 40, 39, 32]]
# \{"district_id": \d, "units_ids": 
region_example_1 = [[179, 172, 102, 120, 228, 100, 215, 156, 306, 155, 212, 270, 177, 234, 211, 305, 191, 233, 190, 118, 175, 210, 197, 174, 209, 138, 173, 207, 101, 288, 157, 198, 216, 139, 196, 213, 208, 195, 252], [307, 2, 1, 129, 109, 50, 37, 76, 34, 289, 3, 60, 89, 69, 312, 309, 163, 199, 32, 19, 127, 88, 85, 5, 73, 130, 87, 57, 165, 293, 83, 93, 4, 33, 218, 217, 128, 166, 235, 107, 23, 80, 67, 124, 308, 201, 186, 237, 27, 84, 7, 49, 62, 47, 46, 91, 71, 42, 70, 311, 310, 182, 123, 145, 74, 51, 44, 61, 43, 271, 313, 185, 6, 24, 75, 21, 272, 141, 200, 253, 125, 184, 66, 181, 48, 35, 45, 22, 219, 41, 55, 183], [38, 56, 58, 40, 59, 20, 39], [266, 230, 248, 265, 226, 267, 245, 247, 227, 284, 246, 264, 283, 229, 263], [202, 115, 204, 134, 223, 169, 203, 132, 222, 205, 150, 168, 114, 187, 116, 133], [79], [317, 287, 258, 286, 314, 214, 296, 319, 290, 260, 277, 318, 259, 316, 269, 315, 295, 294, 322, 292, 304, 321, 250, 291, 278, 232, 249, 276, 275, 268, 285, 297, 324, 323, 274, 251, 261, 231, 320], [273, 300, 189, 171, 299, 117, 240, 257, 112, 99, 135, 96, 224, 221, 262, 63, 152, 280, 149, 119, 131, 188, 303, 82, 244, 302, 167, 256, 81, 243, 236, 95, 137, 164, 94, 151, 279, 65, 110, 92, 301, 220, 242, 148, 206, 78, 241, 298, 147, 113, 170, 255, 281, 98, 254, 225, 282, 97, 154, 77, 153, 111, 136, 239, 146, 238, 64], [17, 31, 159, 158, 30, 28, 86, 143, 15, 178, 142, 14, 106, 105, 162, 16, 161, 144, 90, 13, 72, 52, 10, 108, 9, 194, 36, 53, 176, 193, 122, 104, 121, 160, 12, 140, 29, 11, 68, 126, 26, 54, 8, 25, 18, 180, 103, 192]]

region_example_2 = [[17, 36, 53, 35, 18], [2, 171, 117, 1, 129, 109, 40, 37, 135, 76, 152, 149, 119, 3, 60, 118, 39, 10, 65, 148, 20, 19,
111, 8, 5, 102, 73, 130, 28, 57, 96, 83, 93, 134, 63, 4, 132, 82, 116, 38, 95, 137, 94, 23, 151, 79, 11, 80, 97, 77, 136, 25, 133, 120, 112, 58, 99, 27, 84, 7, 62, 131, 47, 46, 81, 56, 92, 114, 91, 101, 78, 42, 153, 64, 74, 44, 61, 43, 100, 6, 24, 75, 21, 59, 115, 9, 45, 22
, 113, 41, 98, 55, 26, 154, 110], [273, 202, 307, 145, 201, 258, 240, 257, 314, 186, 237, 271, 168, 185,
 296, 313, 165, 293, 224, 204, 221, 290, 203, 260, 277, 272, 289, 218, 259, 188, 200, 217, 315, 187, 295, 256, 128, 167, 236, 253, 294, 223, 312, 184, 166, 235, 292, 309, 222, 181, 164, 279, 274, 291, 220, 163, 278, 150, 242, 219, 276, 206, 199, 241, 298, 275, 147, 170, 255
, 127, 297, 169, 254, 311, 183, 225, 205, 310, 182, 239, 146, 308, 238], [49, 12, 29, 31, 66, 68, 85, 30
, 48, 67, 13, 50, 14, 32], [179, 172, 189, 230, 159, 228, 158, 215, 227, 156, 214, 143, 178, 155, 212, 142, 177, 234, 211, 191, 233, 162, 190, 144, 161, 141, 175, 210, 197, 174, 209, 138, 125, 194, 176, 193, 250, 173, 207, 232, 249, 121, 229
, 160, 140, 157, 198, 216, 226, 139, 196, 213, 126, 208, 195, 124, 251, 180, 231, 192], [51, 34, 16, 33,
 15, 52], [300, 317, 248, 299, 245, 284, 283, 263, 262, 319, 280, 318, 247, 316, 246, 303, 244, 302, 266
, 243, 265, 322, 321, 301, 282, 264, 281, 261, 320], [106, 71, 108, 70, 88, 105, 107, 72, 87, 90, 122, 54, 86, 104, 89, 123, 69, 103], [305, 268, 285, 287, 267, 324, 286, 304, 323, 252, 269, 306, 270, 288]]

region_example_3 = [[273, 307, 201, 258, 240, 257, 237, 271, 293, 290, 272, 289, 218, 259, 200, 217, 256, 236, 253, 223, 235, 292, 309, 222, 291, 220, 219, 276, 199, 241, 275, 255, 254, 182, 239, 310, 274, 308, 238], [145, 202, 100, 117, 129, 186, 168, 185, 165, 135, 204, 221, 134, 152, 203, 132, 149, 119, 131, 188, 118, 187, 116, 167, 128, 166, 184, 164, 181, 151, 163, 150, 148, 170, 147, 127, 169, 183, 205, 153, 146, 133], [300, 230, 287, 248, 286, 215, 158, 284, 214, 306, 283, 270, 305, 234, 177, 319, 233, 247, 269, 303, 302, 266, 265, 322, 304, 321, 250, 176, 301, 232, 249, 288, 268, 285, 216, 267, 324, 213, 196, 282, 323, 252, 195, 264, 251, 231, 320], [74, 73, 130, 2, 112, 1, 58, 109, 40, 57, 37, 96, 76, 93, 24, 75, 4, 21, 3, 60, 59, 39, 38, 95, 56, 94, 23, 92, 22, 114, 91, 20, 78, 113, 19, 41, 55, 77, 111, 5, 110], [44, 61, 43, 99, 28, 27, 7, 6, 63, 62, 82, 46, 81, 115, 9, 45, 79, 42, 98, 80, 97, 26, 8, 25], [172, 189, 171, 228, 245, 227, 156, 155, 212, 263, 224, 211, 191, 190, 246, 175, 210, 244, 174, 209, 138, 243, 137, 194, 193, 173, 207, 229, 206, 157, 226, 139, 208, 225, 154, 136, 192], [317, 299, 314, 296, 313, 262, 280, 260, 277, 318, 316, 315, 295, 294, 312, 279, 278, 242, 298, 297, 311, 281, 261], [17, 179, 102, 159, 120, 87, 86, 143, 178, 84, 142, 106, 83, 105, 162, 144, 161, 90, 141, 72, 89, 69, 197, 52, 108, 125, 107, 36, 53, 122, 35, 104, 121, 101, 71, 160, 140, 70, 198, 88, 68, 85, 126, 124, 54, 18, 123, 180, 103], [51, 31, 30, 15, 50, 14, 49, 34, 16, 33, 13, 47, 10, 66, 48, 65, 32, 12, 29, 11, 67, 64]]

region_example_4 = [[44, 61, 172, 189, 120, 171, 100, 117, 43, 99, 156, 28, 133, 155, 27, 7, 96, 135, 83, 134, 191, 152, 63, 24, 6, 132, 136, 190, 119, 62, 188, 60, 118, 175, 47, 82, 116, 174, 46, 81, 138, 115, 10, 137, 9, 151, 193, 65, 173, 150, 207, 79, 45, 114, 101, 78, 170, 42, 29, 192, 98, 139, 208, 97, 154, 80, 26, 153, 8, 25, 5, 64], [273, 202, 307, 201, 237, 271, 168, 185, 165, 221, 290, 203, 149, 272, 289, 218, 200, 217, 167, 256, 236, 253, 166, 184, 235, 164, 181, 292, 309, 291, 220, 219, 148, 199, 147, 255, 254, 183, 182, 274, 308, 238], [179, 159, 158, 215, 214, 143, 178, 142, 177, 234, 162, 144, 161, 197, 194, 176, 160, 157, 198, 216, 196, 213, 126, 195, 180, 231], [17, 51, 102, 31, 30, 87, 86, 15, 50, 84, 14, 49, 106, 105, 34, 16, 33, 90, 13, 72, 89, 69, 108, 125, 66, 107, 36, 53, 48, 122, 35, 104, 121, 71, 32, 12, 70, 88, 11, 68, 85, 67, 124, 54, 18, 52, 103], [317, 258, 299, 240, 257, 314, 186, 296, 313, 293, 263, 224, 204, 262, 280, 260, 277, 259, 316, 187, 315, 295, 243, 294, 223, 312, 222, 279, 278, 242, 276, 206, 241, 298, 275, 297, 169, 311, 205, 310, 239, 281, 261], [300, 287, 286, 284, 306, 270, 305, 319, 233, 318, 269, 303, 302, 322, 304, 321, 250, 301, 232, 249, 288, 268, 285, 267, 324, 323, 252, 251, 320], [209, 266, 211, 244, 230, 248, 265, 226, 228, 245, 247, 225, 282, 227, 246, 264, 210, 283, 212, 229], [145, 74, 73, 130, 2, 112, 129, 1, 58, 109, 40, 57, 37, 76, 93, 75, 4, 21, 131, 3, 59, 39, 128, 38, 95, 56, 94, 23, 163, 92, 22, 91, 20, 113, 19, 127, 41, 55, 77, 111, 146, 110], [123, 140, 141]]

def visualize_iteration():
    fig, ax1 = plt.subplots(figsize=(6, 8))

    checkerboard_table(ax1, region_example_4)

    plt.tight_layout(pad=2, w_pad=0, h_pad=4.0)
    # plt.gcf().subplots_adjust(top=0.9)
    plt.gcf().subplots_adjust(bottom=0.2)
    plt.show()


def find_district_id_by_unit_id(region, unit_id):
    for i, district in enumerate(region):
        if unit_id in district:
            return i + 1
    raise KeyError


def get_color_patches(colors):
    patches = []
    for i, color in enumerate(colors):
        patches.append(mpatches.Patch(color=color, label='District ' + str(i + 1)))
    return patches


def checkerboard_table(ax, region, fmt='{:.2f}'):
    loaded_region = region
    nrows = 18
    ncolumns = 18
    ax.set_axis_off()
    tb = Table(ax, bbox=[0, 0, 1, 1])
    colors = COLORS[:len(loaded_region)]
    width, height = 1.0 / ncolumns, 1.0 / nrows

    # Add cells
    row_index = 1
    for unit_id in range(1, 18 * 18 + 1):
        column_index = unit_id % ncolumns
        column_index = column_index if column_index != 0 else ncolumns

        color_id = find_district_id_by_unit_id(loaded_region, unit_id)
        color = colors[color_id - 1]

        # facecolor - background color
        tb.add_cell(row_index, column_index, width, height,
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


if __name__ == "__main__":
    visualize_iteration()
