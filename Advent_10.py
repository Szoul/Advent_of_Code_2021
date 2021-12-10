with open("Advent_10_Input.txt", "r") as text_file:
    text_lines = text_file.read().split("\n")

"""
lines consist of (), [], {} and <>
valid: ([[]]), (<{{[[]]}}>), [()()()], ... 
invalid: (([{]])), (<<()>>}, [()[())()], ...
incomplete: (([[]]), {(<>)[<()>], ...

value: ) = 3,   ] = 57,   } = 1197,   > = 25137
    > illegal always has to be a closing parenthesis
"""
# Part 1:   Discard all incomplete lines for now, find the first illegal character
#           return the sum_of_all_corrupted_lines(value_of_the_first_illegal_character)

syntax_error_score = 0
incomplete_shortened_lines = []
for line in text_lines:
    while "()" in line or "[]" in line or "{}" in line or "<>" in line:
        line = line.replace("()", "")
        line = line.replace("[]", "")
        line = line.replace("{}", "")
        line = line.replace("<>", "")
    for parenthesis in line:
        if parenthesis == ")":
            syntax_error_score += 3
            break
        elif parenthesis == "]":
            syntax_error_score += 57
            break
        elif parenthesis == "}":
            syntax_error_score += 1197
            break
        elif parenthesis == ">":
            syntax_error_score += 25137
            break
        else:
            continue
    if not (")" in line or "]" in line or "}" in line or ">" in line):
        incomplete_shortened_lines.append(line)
print(f"Part 1: Syntax error score = {syntax_error_score}")


"""
How to calculate score for completing parenthesis of a single line:
    value: ) = 1,   ] = 2,   } = 3,   > = 4 
    iterate through the completing parenthesis in order
    start at 0 -> first multiply by 5 each iteration and then add the value
"""
# Part 2:   Discard all corrupted lines, find out the sequence of closing parenthesis for all incomplete lines
#           calculate score_of_completing_parenthesis for each line
#           return the middle score out of the above list

list_of_scores = []
for line in incomplete_shortened_lines:
    current_score = 0
    for parenthesis in line[::-1]:
        current_score *= 5
        if parenthesis == "(":
            current_score += 1
        elif parenthesis == "[":
            current_score += 2
        elif parenthesis == "{":
            current_score += 3
        elif parenthesis == "<":
            current_score += 4
        else:
            print("error")
    list_of_scores.append(current_score)

from statistics import median
middle_number = median(list_of_scores)
print(f"Part 2: Middle number = {middle_number}")