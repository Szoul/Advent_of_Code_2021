import copy

with open("Advent_4_Input.txt", "r") as text_file:
    text_list = text_file.read().split("\n")
    drawn_numbers = list(map(int, text_list[0].split(",")))
    ungrouped_board_list = text_list[2:]
    horizontal_board_list = []
    current_board = []
    for row in ungrouped_board_list:                            # requires a newline at the end of text file to work
        if row != "":
            row = list(map(int, row.split()))
            current_board.append(row)
        else:
            horizontal_board_list.append(current_board)
            current_board = []


# Part 1: find the first bingo board that wins if we go through the drawn_numbers,
#         return (winning board unmarked numbers sum)*(winning number)
#         only horizontal and vertical lines count, diagonals aren't considered in this game

vertical_board_list = []
for horizontal_bingo_board in horizontal_board_list:
    vertical_bingo_board = [[] for _ in range(5)]
    for horizontal_line in horizontal_bingo_board:
        for i, bingo_number in enumerate(horizontal_line):
            vertical_bingo_board[i].append(bingo_number)
    vertical_board_list.append(vertical_bingo_board)


def bingo_game(drawn_number):
    numbers = drawn_numbers[0:drawn_number]
    for board_index, board in enumerate(vertical_board_list):
        for line in board:
            if set(line).issubset(numbers):
                vertical_board_boolean = True
                return line, board_index, vertical_board_boolean
    for board_index, board in enumerate(horizontal_board_list):
        for line in board:
            if set(line).issubset(numbers):
                vertical_board_boolean = False
                return line, board_index, vertical_board_boolean
    return None, None, None


for x in range(len(drawn_numbers)):
    winning_line, i, vert_board = bingo_game(x)
    if winning_line is not None:

        winning_board = vertical_board_list[i]
        uncrossed_numbers_sum = 0
        for lines in winning_board:
            for number in lines:
                if number not in drawn_numbers[:x]:
                    uncrossed_numbers_sum += number

        print(f"Part 1: Uncrossed number sum of the winning board multiplied by the winning number"
              f" = {uncrossed_numbers_sum*drawn_numbers[x-1]}")
        break


""" debugging:
    all initial lists are correct (horizontal, vertical and drawn numbers)
    
    possible problems:  >list [0:x] with x being one too low/high<
                        set.issubset() function not working as i intended
                        >sum/ end calculation faulty<
    
    better solution paths:  better system to work with 2-Dimensional Maps?
                            >try out this algorithm with the example<
    
    
    -> Try out example:
        solution wrong
        does not add last board ?
        > Solution: newline at end required for else clause to work at the last iteration
        Calculation wrong
        > requires sum of all non marked numbers * winning number (i read it wrong)
        > Right solution implemented
        >>> WORKS!
        >>> Solution correct <<<
"""

# Part 2: Same, but this time we are trying to find the last board to achieve a bingo, Solution Calculation identical


def mostly_copied_because_i_am_lazy(drawn_number):
    numbers = drawn_numbers[0:drawn_number]
    for board_index, board in enumerate(reduced_vertical_board_list):
        for line in board:
            if set(line).issubset(numbers):
                vertical_board_boolean = True
                return line, board_index, vertical_board_boolean
    for board_index, board in enumerate(reduced_horizontal_board_list):
        for line in board:
            if set(line).issubset(numbers):
                vertical_board_boolean = False
                return line, board_index, vertical_board_boolean
    return None, None, None


reduced_horizontal_board_list = copy.deepcopy(horizontal_board_list)
reduced_vertical_board_list = copy.deepcopy(vertical_board_list)
for_loop_break_condition = False
for x in range(len(drawn_numbers)):
    while True:
        winning_line, i, vert_board = mostly_copied_because_i_am_lazy(x)

        if winning_line is not None and len(reduced_vertical_board_list) > 1:
            reduced_horizontal_board_list.remove(reduced_horizontal_board_list[i])
            reduced_vertical_board_list.remove(reduced_vertical_board_list[i])
            continue

        elif winning_line is not None and len(reduced_vertical_board_list) == 1:
            winning_board = reduced_vertical_board_list[i]
            uncrossed_numbers_sum = 0
            for lines in winning_board:
                for number in lines:
                    if number not in drawn_numbers[:x]:
                        uncrossed_numbers_sum += number

            print(f"Part 2: Uncrossed number sum of the last board multiplied by the last board winning number"
                  f" = {uncrossed_numbers_sum*drawn_numbers[x-1]}")
            for_loop_break_condition = True
            break
        else:
            break

    if for_loop_break_condition:
        break

"""
possible problems: multiple boards win in a single iteration, but not all get crossed out
it loops through the whole drawn numbers list, but there are still a few boards left at the end
(which should not happen)
-> maybe implement while loop (and remove list piece each iteration) under line 107 until the function returns None
>>> works, solution correct, working spaghetti code achieved <<<
"""