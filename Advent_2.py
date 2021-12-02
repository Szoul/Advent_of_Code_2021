with open("Advent_2_Input.txt", "r") as text_file:
    text_list = text_file.read().split("\n")
    if text_list[-1] == "":                                     # text editor keeps adding a new empty line at the end
        text_list = text_list[:-1]


# part 1
depth = 0
horizontal_position = 0

for command in text_list:
    if command.startswith("forward"):
        horizontal_position += int(command[7:])
    elif command.startswith("down"):
        depth += int(command[4:])
    elif command.startswith("up"):
        depth -= int(command[2:])

print(f"part 1: depth = {depth} horizontal position = {horizontal_position} product = {depth * horizontal_position}")


# part 2
aim = 0
horizontal_position = 0
depth = 0

for command in text_list:
    if command.startswith("forward"):
        nmb = int(command[7:])
        horizontal_position += nmb
        depth += aim*nmb
    elif command.startswith("down"):
        aim += int(command[4:])
    elif command.startswith("up"):
        aim -= int(command[2:])

print(f"part 2: depth = {depth} horizontal position = {horizontal_position} product = {depth * horizontal_position}")

