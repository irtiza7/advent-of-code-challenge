def foo(char_index, adjacent_lines):
    is_number_valid = False
    index_of_gear_symbol = None

    for index in range(-1, 2):
        line = adjacent_lines[index + 1]
        indexes_to_examine = [char_index]

        if char_index != 0:
            indexes_to_examine.append(char_index - 1)
        
        if char_index != len(adjacent_lines[0]):
            indexes_to_examine.append(char_index + 1)

        for index_to_examine in indexes_to_examine:
            if line[index_to_examine] in SYMBOLS:
                is_number_valid = True

                if line[index_to_examine] == GEAR_SYMBOL:
                    # print("hui")
                    index_of_gear_symbol = [index, index_to_examine]

    return (is_number_valid, index_of_gear_symbol)

def examine_adjacent_characters(char_index, adjacent_lines):
    for line in adjacent_lines:
        if line[char_index - 1] in SYMBOLS or line[char_index] in SYMBOLS or line[char_index + 1] in SYMBOLS:
            return True
    return False

def calculate_sum_of_part_numbers(lines):
    sum = 0
    gears = {}

    for line_index in range(len(lines)):
        current_line = lines[line_index]
        prev_line = lines[line_index - 1] if line_index != 0 else ["." for i in range(len(current_line))]
        next_line = lines[line_index + 1] if line_index + 1 < len(lines) else ["." for i in range(len(current_line))]

        adjacent_lines = [prev_line, current_line, next_line]

        partNumber = ""
        isValidPartNumber = False
        index_of_gear_symbol = None

        for char_index in range(len(current_line)):
            char = current_line[char_index]

            if char.isdigit():
                partNumber += char

                number_validity, index_of_gear_symbol = foo(char_index, adjacent_lines)
                isValidPartNumber = isValidPartNumber or number_validity

                if index_of_gear_symbol: 
                    # line number: -1 means prev line, 0 means current line, 1 means next line
                    line_number_of_gear = index_of_gear_symbol[0] 
                    index_of_gear_symbol[0] = line_index + line_number_of_gear
                    print(index_of_gear_symbol)

            if char == '.' or char in SYMBOLS:
                if index_of_gear_symbol:
                    gear_info = (index_of_gear_symbol[0], index_of_gear_symbol[1])
                    gears[gear_info] = int(partNumber)
                elif isValidPartNumber:
                    sum += int(partNumber)
                
                isValidPartNumber = False
                partNumber = ""
                index_of_gear_symbol = None

            if char_index + 2 == len(current_line):
                if current_line[char_index + 1].isdigit():
                    partNumber += current_line[char_index + 1]
                   
                    if index_of_gear_symbol:
                        gear_info = (index_of_gear_symbol[0], index_of_gear_symbol[1])
                        gears[gear_info] = int(partNumber)
                    elif isValidPartNumber:
                        sum += int(partNumber)
                    break
    for key,val in gears.items():
        nums = val
        # print(nums)

    return sum

SYMBOLS = "!@#$%^&*()_+-=|<>,:;/"
GEAR_SYMBOL = '*'

with open("./input.txt") as file:
    lines = file.read().split("\n")
    print(f"Sum: {calculate_sum_of_part_numbers(lines)}")