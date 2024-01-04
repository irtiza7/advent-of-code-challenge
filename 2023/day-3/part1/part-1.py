def examine_adjacent_characters(char_index, adjacent_lines):
    for line in adjacent_lines:
        if line[char_index - 1] in SYMBOLS or line[char_index] in SYMBOLS or line[char_index + 1] in SYMBOLS:
            return True
    return False

def calculate_sum_of_part_numbers(lines):
    sum = 0
    for line_index in range(len(lines)):
        current_line = lines[line_index]
        prev_line = lines[line_index - 1] if line_index != 0 else ["." for i in range(len(current_line))]
        next_line = lines[line_index + 1] if line_index + 1 < len(lines) else ["." for i in range(len(current_line))]

        adjacent_lines = [current_line, prev_line, next_line]

        partNumber = ""
        isValidPartNumber = False

        for char_index in range(len(current_line)):
            char = current_line[char_index]

            if char.isdigit():
                partNumber += char
                isValidPartNumber = isValidPartNumber or examine_adjacent_characters(char_index, adjacent_lines)

            if char == '.' or char in SYMBOLS:
                if isValidPartNumber:
                    sum += int(partNumber)
                isValidPartNumber = False
                partNumber = ""

            if char_index + 2 == len(current_line):
                if current_line[char_index + 1].isdigit():
                    partNumber += current_line[char_index + 1]
                    if isValidPartNumber:
                        sum += int(partNumber)
                    break
    return sum

SYMBOLS = "!@#$%^&*()_+-=|<>,:;/"
with open("../input.txt") as file:
    lines = file.read().split("\n")
    print(f"Sum: {calculate_sum_of_part_numbers(lines)}")