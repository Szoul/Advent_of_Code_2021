with open("Advent_13_Input.txt", "r") as text_file:
    text = text_file.read()
    string_coordinates = text.split("\n\n")[0].split("\n")
    initial_positions_list = []
    for string_coordinate in string_coordinates:
        init_position = list(map(int, string_coordinate.split(",")))
        initial_positions_list.append(init_position)
    string_instructions = text.split("\n\n")[1].split("\n")
    string_instruction_list = []
    for string_instruction in string_instructions:
        list_instruction = string_instruction.split()[2].split("=")
        string_instruction_list.append(list_instruction)

"""
        Coordinates [x, y] represent "dots" on a 2D-Map
        instruction [axis, position] define the line on the map where the map gets "folded"
        if axis = y -> fold the bottom half under the y-axis up (though technically it doesnt matter which direction)
        if axis = x -> fold the right half onto the left at the x-axis defined
        -> overlapping dots after a fold get "merged" into a single coordinate
        -> a dot will never be on a folding line itself
"""


# Part 1:   return number of dots after the first fold


def fold(coordinates, instruction):
    if instruction[0] == "x":
        folding_axis = 0
    else:
        folding_axis = 1
    folding_line = int(instruction[1])
    new_coordinates = []

    for coordinate in coordinates:
        if coordinate[folding_axis] < folding_line:
            new_coordinate = coordinate
        else:
            changed_axis_value = coordinate[folding_axis] - ((coordinate[folding_axis] - folding_line) * 2)
            new_coordinate = coordinate
            new_coordinate[folding_axis] = changed_axis_value

        if new_coordinate in new_coordinates:
            pass
        else:
            new_coordinates.append(new_coordinate)

    return new_coordinates


new_map = fold(initial_positions_list, string_instruction_list[0])
print(f"Part 1: number of dots after the first fold = {len(new_map)}")

# Part 2:   once all instructions are completed, the resulting dots should show 8 Capital letters
#           return these letters

new_map = initial_positions_list
for i, folding_instruction in enumerate(string_instruction_list):
    new_map = fold(new_map, folding_instruction)
max_y = 0
max_x = 0
for dot in new_map:
    if dot[0] > max_x:
        max_x = dot[0]
    if dot[1] > max_y:
        max_y = dot[1]

print("Part 2: 8 Letter Codeword:")
for y in range(max_y + 1):
    for x in range(max_x + 1):
        if x % 5 == 0 and x != 0:
            print("\033[1;30m____", end="")
        if [x, y] in new_map:
            print("\033[2;32m0", end="")
        else:
            print("\033[1;30m_", end="")
    print("\033[2;39m")
