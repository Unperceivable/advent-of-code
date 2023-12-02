"""Solutions to https://adventofcode.com/2023/day/1 Puzzles."""


import re
from pathlib import Path


def trebuchet(calibration_text: list[str]):
    """Returns the sum of all concatenated f'{first}{last}' digits in each line of a multiline text file.

    For example:

    1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet

    In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.
    """
    calibration_values = []
    for line in calibration_text:
        digit_pattern = re.compile(r"\d")
        matches = digit_pattern.findall(line)
        if matches:
            first_digit = matches[0]
            last_digit =  matches[-1]
            calibration_values.append(int(f"{first_digit}{last_digit}"))
        else:
            raise ValueError(f"{line} doesnt contain any digits")
    return sum(calibration_values)

def improved_trebuchet(calibration_text: list[str]):
    """Returns the sum of all concatenated f'{first}{last}' digits in each line of a multiline text file, where spelled digits one-nine are valid.

    For example:

    two1nine
    eightwothree
    abcone2threexyz
    xtwone3four
    4nineeightseven2
    zoneight234
    7pqrstsixteen

    In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.
    """
    digit_map = {
    "one": 1,
    "1": 1,
    "two": 2,
    "2": 2,
    "three": 3,
    "3": 3,
    "four": 4,
    "4": 4,
    "five": 5,
    "5": 5,
    "six": 6,
    "6": 6,
    "seven": 7,
    "7": 7,
    "eight": 8,
    "8": 8,
    "nine": 9,
    "9": 9
}

    calibration_values = []
    for line in calibration_text:
        digit_pattern = re.compile(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))")
        matches = digit_pattern.findall(line)
        if matches:
            first_digit = digit_map[matches[0]]
            last_digit = digit_map[matches[-1]]
            calibration_values.append(int(f"{first_digit}{last_digit}"))
        else:
            raise ValueError(f"Value: '{line}' doesnt contain any digits")
    return sum(calibration_values)

if __name__ == "__main__":
    calibration_text_path = Path("trebuchet.txt")
    with open(calibration_text_path) as calibration_text:
        print(f"Calibration Value: {trebuchet(calibration_text)}")
        print(f"Improved Calibration Value: {improved_trebuchet(calibration_text)}")