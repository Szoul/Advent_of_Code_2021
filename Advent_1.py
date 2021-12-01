with open ("Advent_1_Input.txt", "r") as text_file:
    text = text_file.read()
    text_list = text.split("\n")
    if text_list[-1] == "":                                     # text editor keeps adding a new empty line at the end
        text_list = text_list[:-1]
    text_list = list(map(int, text_list))


# first puzzle
def count_increases(number_list):
    count = 0
    for i, value in enumerate(number_list):
        if value == number_list[-1]:
            return count
        elif number_list[i+1] > value:
            count += 1


print(count_increases(text_list))


# second puzzle
three_measurement_list = []
for x, unused in enumerate(text_list):
    nmb = text_list[x] + text_list[x+1] + text_list[x+2]
    three_measurement_list.append(nmb)
    if x == len(text_list)-3:
        break

print(count_increases(three_measurement_list))

