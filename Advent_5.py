with open("Advent_5_Input.txt", "r") as text_file:
    text_lines = text_file.read().split("\n")
    if text_lines[-1] == "":
        text_lines = text_lines[:-1]
    vent_position_list = []
    vent_position_list_horizontal_and_vertical = []
    for line in text_lines:
        vent_position_string = line.split(" -> ")
        x_one, y_one = vent_position_string[0].split(",")
        x_two, y_two = vent_position_string[1].split(",")
        vent_position_list.append([(int(x_one), int(y_one)), (int(x_two), int(y_two))])
        if x_one == x_two or y_one == y_two:
            vent_position_list_horizontal_and_vertical.append([(int(x_one), int(y_one)), (int(x_two), int(y_two))])

# Part 1:   Consider only horizontal/vertical lines: [580,438 -> 580,817] meaning every point x,y from y = 438 to 817
#           is marked (x= 580);
#           solution: count: everywhere where at least 2 lines overlap
#           Numbers range from 0-999, meaning a 1000x1000 coordinate System is sufficient


def add_one_line_of_vents_to_coordinate_system(vent_line, c_system):
    x_one_pos, y_one_pos = vent_line[0]
    x_two_pos, y_two_pos = vent_line[1]

    if x_one_pos == x_two_pos:
        if y_two_pos > y_one_pos:
            direction = 1
        else:
            direction = -1
        for y in range(y_one_pos, (y_two_pos+direction), direction):
            c_system[x_one_pos][y] += 1

    elif y_one_pos == y_two_pos:
        if x_two_pos > x_one_pos:
            direction = 1
        else:
            direction = -1
        for x in range(x_one_pos, (x_two_pos+direction), direction):
            c_system[x][y_one_pos] += 1

    # this assumes that the x difference and the y difference is always equally large, meaning
    # that every point on the diagonal line is also a point in the coordinate system
    # (line is 45 degrees to horizontal/vertical lines)
    else:
        if x_one_pos > x_two_pos:
            x_direction = -1
        else:
            x_direction = 1
        if y_one_pos > y_two_pos:
            y_direction = 1
        else:
            y_direction = -1

        difference = (y_one_pos-y_two_pos)
        iteration = 0
        for x_position in range(x_one_pos, (x_two_pos+x_direction), x_direction):
            y_position = y_two_pos+difference+iteration
            iteration -= y_direction
            c_system[x_position][y_position] += 1

    return c_system


coordinate_system = [[0 for _ in range(1000)] for _ in range(1000)]
for line in vent_position_list_horizontal_and_vertical:
    coordinate_system = add_one_line_of_vents_to_coordinate_system(line, coordinate_system)
counter = 0
for line in coordinate_system:
    for number in line:
        if number >= 2:
            counter += 1
print(f"Part 1: number of overlapping positions = {counter}")


# Part 2: Same, but this time we consider diagonal input too
coordinate_system_2 = [[0 for _ in range(1000)] for _ in range(1000)]
for line in vent_position_list:
    coordinate_system = add_one_line_of_vents_to_coordinate_system(line, coordinate_system_2)
counter = 0
for line in coordinate_system:
    for number in line:
        if number >= 2:
            counter += 1
print(f"Part 2: number of overlapping positions, including diagonals = {counter}")
