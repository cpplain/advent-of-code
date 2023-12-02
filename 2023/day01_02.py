# Advent of Code 2023

# Day 1: Trebuchet?!
# Part Two
# Combine fist and last digit of each line in doc and sum.
# Digit could be spelled.

# Test input
# 29, 83, 13, 24, 42, 14, and 76 sum equals 281
#
# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen


def sum_calibration(doc):
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    sum = 0
    with open(doc) as f:
        lines = f.readlines()
        for line in lines:
            first_num, last_num = "", ""
            first_index, last_index = float("inf"), float("-inf")

            digits = "".join(filter(str.isdigit, line))
            if len(digits) > 0:
                first_num, last_num = digits[0], digits[len(digits) - 1]
                first_index = line.index(first_num)
                last_index = line.rindex(last_num)

            for i, num in enumerate(numbers, start=1):
                if num not in line:
                    continue

                l_index = line.index(num)
                r_index = line.rindex(num)

                if l_index < first_index:
                    first_num = i
                    first_index = l_index

                if r_index > last_index:
                    last_num = i
                    last_index = r_index

            sum += int(first_num) * 10 + int(last_num)
    return sum


test_result = sum_calibration("day01_02_test_input")
print(f"Sum of test input calibration values: {test_result}")

puzzle_result = sum_calibration("day01_puzzle_input")
print(f"Sum of puzzle input calibration values: {puzzle_result}")