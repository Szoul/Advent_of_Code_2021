with open("Advent_4_Input.txt", "r") as text_file:
    text_list = text_file.read().split("\n")
    if text_list[-1] == "":                         # text editor adds a new empty line at the end
        text_list = text_list[:-1]
    drawn_numbers = list(map(int, text_list[0].split(",")))
    ungrouped_board_list = text_list[2:]
    horizontal_board_list = []
    current_board = []
    for row in ungrouped_board_list:
        if row != "":
            row = list(map(int, row.split()))
            current_board.append(row)
        else:
            horizontal_board_list.append(current_board)
            current_board = []


# Part 1: find the first bingo board that wins if we go through the drawn_numbers, return winning row sum*winning number
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
    for board in vertical_board_list:
        for line in board:
            if set(line).issubset(numbers):
                return line
    for board in horizontal_board_list:
        for line in board:
            if set(line).issubset(numbers):
                return line
    return None


for x in range(len(drawn_numbers)):
    winning_line = bingo_game(x)
    if winning_line is not None:
        break

print(winning_line, x, sum(winning_line)*(x+1))
