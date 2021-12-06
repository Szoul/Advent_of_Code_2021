import copy
from collections import Counter

with open("Advent_6_Input.txt", "r") as text_file:
    initial_state = list(map(int, text_file.read().split(",")))

# Part 1:
# each lanternfish creates a new one every 7 days (counted from 6 to 0), independently of other fish
# a newly produced fish has an initial timer of 9 days (counted from 8 to 0) on its first reproduction cycle
# Number of Fish after 80 days = ?

# i guess brute force will still work initially :)


def pass_a_day(current_state):
    new_state = []
    for day in current_state:
        if day == 0:
            new_state.append(6)
            new_state.append(8)
        else:
            new_state.append(day-1)

    return new_state


state = copy.deepcopy(initial_state)
for _ in range(80):
    state = pass_a_day(state)

print(f"Part 1: Number of fish after 80 days = {len(state)}")


# Part 2: EXPONENTIAL GROWTH: return the number after 256 days
# no brute force with this :(
fish_dict = Counter(initial_state)
for x in range(9):
    if x not in fish_dict.keys():
        fish_dict[x] = 0


def pass_a_day_via_dict(dictionary):
    new_dict = {8: dictionary[0], 6: dictionary[0]}
    for days_left in dictionary.keys():
        if days_left == 0:
            pass
        elif days_left == 7:
            new_dict[6] += dictionary[7]
        else:
            new_dict[days_left-1] = dictionary[days_left]

    return new_dict


for _ in range(256):
    fish_dict = pass_a_day_via_dict(fish_dict)
total_fish = 0
for fish in fish_dict.values():
    total_fish += fish

print(f"Part 2: Number of fish after 256 days = {total_fish}")
