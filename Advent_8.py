with open("Advent_8_Input.txt", "r") as text_file:
    text_line = text_file.read().split("\n")
    if text_line[-1] == "":
        text_line = text_line[:-1]
    input_list = []
    all_output_values = []
    for line in text_line:
        signal_pattern = line.split("|")[0].split()
        output_value = line.split("|")[1].split()
        input_list.append([signal_pattern, output_value])
        all_output_values.extend(output_value)

"""
    Seven-Segment-Display:
           Example:     acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
                        cdfeb fcadb cdfeb cdbaf
                        
                        > first line is possible Input, each "word" represents a number from 0-9
                        > the length of the word corresponds to the lines in a Seven-Segment-Display
                        > Example: number 1 is the only one represented by 2 letters; unique numbers are 1,4,7,8
                        > 0 = 6 | 1 = 2 | 2 = 5 | 3 = 5 | 4 = 4 | 5 = 5 | 6 = 6 | 7 = 3 | 8 = 7 | 9 = 6 
                        > the second line is the Output value (what is actually shown on the display)
                        > the Order of letters might be different, but the same letters are needed to express 
                          a certain number
                        > in this example: all are 5 letters long, meaning it could stand for 2, 3 or 5
                        > we can deduce the arrangement of letters each representing a line in the S-S-Display
"""

#  Part 1:  return sum(number_of_all_output_values_with_easy_digits) for all lines
#           easy letters == 1, 4, 7, 8 with respective letter_length == 2, 4, 3, 7

sum_of_easy_output_values = 0
for letter in all_output_values:
    length = len(letter)
    if length in [2, 4, 3, 7]:
        sum_of_easy_output_values += 1
print(f"Part 1: Sum of the number of all easy output values = {sum_of_easy_output_values}")

# Part 2:   return sum(all_output_values_converted_to_int) for all lines
"""
    length of 6: 0,6,9
        0 has to contain same letters as: [1, 7] 8
        6 has to contain same letters as: [5] 8
        9 has to contain same letters as: [1, 3, 4, 5, 7] 8
    length of 5: 2,3,5
        2 has to contain same letters as: 8
        3 has to contain same letters as: [1, 7] 8, 9
        5 has to contain same letters as: 6, 8, 9
    > 8 contains every letter since it occupies all 7 Signals
    > numbers in brackets [] are subsets of the left number, left number is subset of numbers not in brackets
    > if length == 5 and it matches exactly 1 other number (and itself) as a subset -> it has to be the code for num 2
    > if length == 6 and it is matched by exactly 3 numbers as them being subsets -> it has to be the code for num 0
"""


def deduce_letter_arrangement_and_corresponding_number(pattern):
    letter_decoder = {}
    for item in pattern:
        if len(item) == 2:
            letter_decoder[item] = 1
        elif len(item) == 4:
            letter_decoder[item] = 4
        elif len(item) == 3:
            letter_decoder[item] = 7
        elif len(item) == 7:
            letter_decoder[item] = 8
        elif len(item) == 5:
            match_counter = 0
            for item_2 in pattern:
                if set(item).issubset(item_2):
                    match_counter += 1
            if match_counter == 2:
                letter_decoder[item] = 2
            elif match_counter == 3:
                letter_decoder[item] = 3
            elif match_counter == 4:
                letter_decoder[item] = 5
            else:
                print(f"error: {item}")
        elif len(item) == 6:
            match_counter = 0
            for item_2 in pattern:
                if set(item_2).issubset(item):
                    match_counter += 1
            if match_counter == 3:
                letter_decoder[item] = 0
            elif match_counter == 2:
                letter_decoder[item] = 6
            elif match_counter == 6:
                letter_decoder[item] = 9
            else:
                print(f"error: {item}")
        else:
            print(f"error: {item}")
    return letter_decoder


sum_of_all_output_values = 0
for pattern_output_set in input_list:
    decoder = deduce_letter_arrangement_and_corresponding_number(pattern_output_set[0])
    codes = pattern_output_set[1]

    whole_number_string = ""
    for code in codes:
        for decode in decoder.keys():
            if set(code) == set(decode):
                number_string = str(decoder[decode])
                break
        whole_number_string += number_string
    whole_number = int(whole_number_string)
    sum_of_all_output_values += whole_number

print(f"Part 2: Sum of all decoded output values = {sum_of_all_output_values}")
