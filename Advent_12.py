with open("Advent_12_Input.txt", "r") as text_file:
    text_lines = text_file.read().split("\n")
    cave_dict = {}
    for line in text_lines:
        first_cave = line.split("-")[0]
        second_cave = line.split("-")[1]
        if first_cave in cave_dict.keys():
            cave_dict[first_cave].append(second_cave)
        else:
            cave_dict[first_cave] = [second_cave]
        if second_cave in cave_dict.keys():
            cave_dict[second_cave].append(first_cave)
        else:
            cave_dict[second_cave] = [first_cave]

"""
            Each string (except for "start" and "end") represents a cave
            Strings in uppercase are big caves, those in lowercase: small caves
            input (transformed here into a dictionary) represents how these caves are connected
"""

# Part 1:   How many different paths can you take from "start" to "end" if you cannot visit a small cave more than once
#           per path taken (logically no 2 big caves are connected)
#           return number of possible paths


def get_paths(part_one=True):
    list_of_all_possible_paths = [["start"]]
    exit_condition = False
    while not exit_condition:
        new_list_of_all_possible_paths = []
        for path in list_of_all_possible_paths:
            current_cave = path[-1]
            if current_cave == "end":
                new_list_of_all_possible_paths.append(path)
                continue

            adjacent_caves = cave_dict[current_cave]
            for cave in adjacent_caves:
                if cave == "start":
                    continue
                if part_one:
                    if not (cave.islower() and cave in path):
                        new_path = [x for x in path]
                        new_path.append(cave)
                        new_list_of_all_possible_paths.append(new_path)
                    else:
                        pass
                elif not part_one:
                    small_cave_visited_twice = False
                    for key in cave_dict.keys():
                        if key.islower():
                            if path.count(key) > 1:
                                small_cave_visited_twice = True
                    if not (cave.islower() and cave in path and small_cave_visited_twice):
                        new_path = [x for x in path]
                        new_path.append(cave)
                        new_list_of_all_possible_paths.append(new_path)
                    else:
                        pass

        list_of_all_possible_paths = new_list_of_all_possible_paths

        for path in new_list_of_all_possible_paths:
            if path[-1] != "end":
                exit_condition = False
                break
            else:
                exit_condition = True
    return list_of_all_possible_paths


part_one_list = get_paths(part_one=True)
print(f"Part 1: Number of possible paths = {len(part_one_list)}")

# Part 2:   new rule: you can now visit a single small cave up to 2 times all other small caves still only once
#           return number of possible paths

part_two_list = get_paths(part_one=False)
print(f"Part 1: Number of possible paths = {len(part_two_list)}")
