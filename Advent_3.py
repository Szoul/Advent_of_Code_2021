with open("Advent_3_Input.txt", "r") as text_file:
    text_list = text_file.read().split("\n")
    if text_list[-1] == "":  # text editor keeps adding a new empty line at the end
        text_list = text_list[:-1]

# part 1
gamma_rate = ""
epsilon_rate = ""

for indentation in range(len(text_list[0])):
    zero_counter = 0
    one_counter = 0
    for x in text_list:
        if x[indentation] == "0":
            zero_counter += 1
        else:
            one_counter += 1

    if zero_counter > one_counter:
        gamma_rate += "0"
        epsilon_rate += "1"
    else:
        gamma_rate += "1"
        epsilon_rate += "0"

print(f"Part 1: epsilon rate = {epsilon_rate}, gamma rate = {gamma_rate}, "
      f"product in int = {int(gamma_rate, 2) * int(epsilon_rate, 2)}")


# part 2:

def i_love_recursion_and_nothing_can_change_my_mind(remaining_list, indent=0, rating="oxygen"):
    if len(remaining_list) == 1:
        return int(remaining_list[0], 2)

    nmb_of_zeros = 0
    nmb_of_ones = 0
    new_list = []
    for binary_number in remaining_list:
        if binary_number[indent] == "0":
            nmb_of_zeros += 1
        else:
            nmb_of_ones += 1

    if (nmb_of_zeros > nmb_of_ones and rating == "oxygen") or (nmb_of_zeros < nmb_of_ones and rating == "CO2"):
        for binary_number in remaining_list:
            if binary_number[indent] == "0":
                new_list.append(binary_number)
    elif (nmb_of_zeros > nmb_of_ones and rating == "CO2") or (nmb_of_zeros < nmb_of_ones and rating == "oxygen"):
        for binary_number in remaining_list:
            if binary_number[indent] == "1":
                new_list.append(binary_number)
    elif nmb_of_zeros == nmb_of_ones and rating == "oxygen":
        for binary_number in remaining_list:
            if binary_number[indent] == "1":
                new_list.append(binary_number)
    else:
        for binary_number in remaining_list:
            if binary_number[indent] == "0":
                new_list.append(binary_number)

    indent += 1
    return i_love_recursion_and_nothing_can_change_my_mind(new_list, indent, rating)


oxygen_generator_rating = i_love_recursion_and_nothing_can_change_my_mind(text_list, 0, "oxygen")
CO2_scrubber_rating = i_love_recursion_and_nothing_can_change_my_mind(text_list, 0, "CO2")
print(f"Part 2: oxygen = {oxygen_generator_rating}, CO2 = {CO2_scrubber_rating}, "
      f"product = {oxygen_generator_rating*CO2_scrubber_rating}")
