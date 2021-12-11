import copy

with open("Advent_11_Input.txt", "r") as text_file:
    text_lines = text_file.read().split("\n")
    input_grid = []
    for lines in text_lines:
        new_line = []
        for string_number in lines:
            new_line.append(int(string_number))
        input_grid.append(new_line)

"""
numbers range from 0 to 9
Rules per step:        Increase all numbers by 1
                       Any number above 9 "activates" -> all adjacent numbers increase by 1
                       Any new number reaching above 9 repeats this process within this step
                       at the end of the step set all numbers that are above 9 to 0
"""
# Part 1: return total number of activations after 100 iterations
flash_counter = 0


def process_one_step(grid):
    global flash_counter
    for y, line in enumerate(grid):
        grid[y] = [x+1 for x in line]

    while True:
        all_numbers_list = []
        for line in grid:
            for number in line:
                all_numbers_list.append(number)

        if not all(number <= 9 for number in all_numbers_list):
            for y, line in enumerate(grid):
                for x, number in enumerate(line):
                    if number > 9:
                        flash_counter += 1
                        grid[y][x] = -10

                        for y_increase in (-1, 0, 1):
                            for x_increase in (-1, 0, 1):
                                if 0 <= y+y_increase <= (len(grid)-1) and 0 <= x+x_increase <= (len(grid[0])-1):
                                    grid[y+y_increase][x+x_increase] += 1
        else:
            break

    for y, line in enumerate(grid):
        for x, number in enumerate(line):
            if number < 0:
                grid[y][x] = 0


part_one_grid = copy.deepcopy(input_grid)
for step in range(100):
    process_one_step(part_one_grid)
print(f"Part 1: Total amount of flashes after 100 steps = {flash_counter}")


# Part 2: return the iteration ("step") number for when the whole grid flashes during its iteration
all_input_numbers = []
for lines in input_grid:
    for num in lines:
        all_input_numbers.append(num)

required_flashes = len(all_input_numbers)
all_flash_condition = False
part_two_grid = copy.deepcopy(input_grid)
step = 0

while not all_flash_condition:
    step += 1
    current_counter = flash_counter
    process_one_step(part_two_grid)
    difference = flash_counter-current_counter
    if difference == required_flashes:
        all_flash_condition = True
print(f"Part 2: Step, on which all flash simultaneously for the first time = {step}")
