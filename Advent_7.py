with open("Advent_7_Input.txt", "r") as text_file:
    initial_position = list(map(int, text_file.read().split(",")))

# Part 1:   These Numbers represent horizontal positions, find the common number that is closest to all of them
#           return the sum of differences ("total fuel used") between all numbers and the goal number


def calculate_fuel_used(init_pos_list, goal_number):
    fuel_used = 0
    for position in init_pos_list:
        fuel_used += abs(position-goal_number)
    return fuel_used


# brute force: numbers range (mostly) in between 0 and 1000
most_efficient_position = 0
for x in range(1000):
    total_diff = calculate_fuel_used(initial_position, x)
    if calculate_fuel_used(initial_position, most_efficient_position) > total_diff:
        most_efficient_position = x
print(f"Part 1: The most efficient Position = {most_efficient_position} with a total fuel used"
      f" of {calculate_fuel_used(initial_position, most_efficient_position)}")


# Part 2: this time a change in initial position costs more the farther it goes [1 = 1, 2 = 3, 3 = 6, x = calc(x-1)+x]
#         again: return most efficient sum of differences with these changed rules


def calculate_fuel_used_2(ini_pos_list, goal_number):
    total_fuel_used = 0
    for position in ini_pos_list:
        diff = abs(position-goal_number)
        fuel_used = 0
        for i in range(diff+1):
            fuel_used += i
        total_fuel_used += fuel_used
    return total_fuel_used


# brute force still works, though significantly slower
# looking at the direction, the closer we get to the goal number the lower the total number becomes (on average)
# allowing an approximation for the in range() function if needed
most_efficient_position = 0
for x in range(1000):
    total_diff = calculate_fuel_used_2(initial_position, x)
    if calculate_fuel_used_2(initial_position, most_efficient_position) > total_diff:
        most_efficient_position = x
print(f"Part 2: The most efficient Position = {most_efficient_position} with a total fuel used"
      f" of {calculate_fuel_used_2(initial_position, most_efficient_position)}")
