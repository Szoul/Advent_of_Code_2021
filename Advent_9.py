with open("Advent_9_Input.txt", "r") as text_file:
    text_line = text_file.read().split("\n")
    heightmap = []
    for line in text_line:
        new_line = []
        for number in line:
            new_line.append(int(number))
        heightmap.append(new_line)


# Part 1: 2-D-Map:  get all low points (points that are horizontally or vertically surrounded by lower numbers
#                   return sum_of_all(low_point+1)


def check_if_low_point(y_position, x_position):
    x_length = len(heightmap[0]) - 1
    y_length = len(heightmap) - 1
    num_to_check = heightmap[y_position][x_position]
    is_low_point = True
    if y_position != 0:
        up_num = heightmap[y_position - 1][x_position]
        if up_num <= num_to_check:
            is_low_point = False
    if y_position != y_length:
        low_num = heightmap[y_position + 1][x_position]
        if low_num <= num_to_check:
            is_low_point = False
    if x_position != 0:
        left_num = heightmap[y_position][x_position - 1]
        if left_num <= num_to_check:
            is_low_point = False
    if x_position != x_length:
        right_num = heightmap[y_position][x_position + 1]
        if right_num <= num_to_check:
            is_low_point = False
    return is_low_point


location_of_low_points = []
sum_of_all_low_point_risk_levels = 0
for y, line in enumerate(heightmap):
    for x, number in enumerate(line):
        if check_if_low_point(y, x):
            sum_of_all_low_point_risk_levels += number + 1
            location_of_low_points.append([y, x])
print(f"Part 1: Sum of all low point risk levels = {sum_of_all_low_point_risk_levels}")

"""
           Each low point is the lowest point of a Basin (consisting of numbers from 0 - 8)
           A basin is defined as: all horizontal/vertical connected numbers that out from the low point are
           increasing outwards
           in this input ALL numbers excluding 9's are part of basins
           -> therefore in order to be definable an area encased by 9's has to be a single basin
Example:    2199943210           2[1]   99943210
            3987894921           3   987894921
            9856789892              9856789   8   92
            8767896789              876789   678   9
            9899965678              98999  6[5]678
"""


# Part 2:   return the product of the 3 largest basins' sizes (size = amount of numbers regardless of value)


def get_basin_size(y_position, x_position):
    basin_position_list = [[y_position, x_position]]
    checked_positions = []
    x_length = len(heightmap[0]) - 1
    y_length = len(heightmap) - 1
    while basin_position_list != checked_positions:
        for location in basin_position_list:
            if location not in checked_positions:
                y_pos = location[0]
                x_pos = location[1]
                if y_pos != 0:
                    if heightmap[y_pos - 1][x_pos] != 9:
                        up_num = [y_pos - 1, x_pos]
                        if up_num not in basin_position_list:
                            basin_position_list.append(up_num)
                if y_pos != y_length:
                    if heightmap[y_pos + 1][x_pos] != 9:
                        low_num = [y_pos + 1, x_pos]
                        if low_num not in basin_position_list:
                            basin_position_list.append(low_num)
                if x_pos != 0:
                    if heightmap[y_pos][x_pos - 1] != 9:
                        left_num = [y_pos, x_pos - 1]
                        if left_num not in basin_position_list:
                            basin_position_list.append(left_num)
                if x_pos != x_length:
                    if heightmap[y_pos][x_pos + 1] != 9:
                        right_num = [y_pos, x_pos + 1]
                        if right_num not in basin_position_list:
                            basin_position_list.append(right_num)
                checked_positions.append(location)
            else:
                pass
    return len(checked_positions)


list_of_basin_sizes = []
for low_point_location in location_of_low_points:
    size = get_basin_size(low_point_location[0], low_point_location[1])
    list_of_basin_sizes.append(size)
sorted_list = sorted(list_of_basin_sizes)
product_of_3_largest_basin_sizes = sorted_list[-1]*sorted_list[-2]*sorted_list[-3]
print(f"Part 2: Product of the size of the 3 largest basins = {product_of_3_largest_basin_sizes}")
