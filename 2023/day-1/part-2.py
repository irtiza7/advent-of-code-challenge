from typing import List, Tuple, Union

numberMappings: dict[str, int] = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def match_word(word: str) -> Union[int, None]:
    matched_number: Union[int, None] = numberMappings.get(word)
    return matched_number


def update_digits(prev_first_digit: int, new_val: int) -> Tuple[int, int]:
    if prev_first_digit == -1:
        return new_val, new_val
    return prev_first_digit, new_val


def extract_digits(lines: List[str]) -> List[int]:
    digits: List[int] = []
    for line in lines:
        first_digit: int = -1
        second_digit: int = -1

        for i in range(len(line)):
            single_char: str = line[i]
            three_char_word: str = line[i : i + 3]
            four_char_word: str = line[i : i + 4]
            five_char_word: str = line[i : i + 5]

            if single_char.isdigit():
                first_digit, second_digit = update_digits(first_digit, int(single_char))
            elif matched_number := match_word(three_char_word):
                first_digit, second_digit = update_digits(first_digit, matched_number)
            elif matched_number := match_word(four_char_word):
                first_digit, second_digit = update_digits(first_digit, matched_number)
            elif matched_number := match_word(five_char_word):
                first_digit, second_digit = update_digits(first_digit, matched_number)

        digits.append((first_digit * 10) + second_digit)
    return digits


with open("./input.txt", "r") as file:
    lines: List[str] = file.read().splitlines()
    digits: List[int] = extract_digits(lines)
    print(f"Sum of {len(digits)} digits from {len(lines)} lines: {sum(digits)}")
