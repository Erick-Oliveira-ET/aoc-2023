import sys
from pathlib import WindowsPath

sys.setrecursionlimit(1500)


def number_mapping(): 
    num_str = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    num_map = {}

    for arr_idx, number_ext in enumerate(num_str):
        temp = num_map

        for idx, char in enumerate(number_ext):
            if char in temp.keys():
                temp = num_map[char]
            else:
                if idx == len(number_ext) - 1:
                    temp[char] = arr_idx + 1 
                else:
                    temp[char] = {}
                    temp = temp[char]
                    
    return num_map

def deep_update(char,first, second):
    if char == 'o' and 'o' in first and 'n' in first[char]:
        second['n'] = dict(first[char]['n'], **second['n'])
        return second
    if char == 'o' and 'o' in second and 'n' in second[char]:
        first['n'] = dict(second[char]['n'], **second['n'])
        return first

    return dict(first, **second)

number_map = number_mapping()

input_path = WindowsPath(".")/ "Day 1" / "input.txt"

raw = open(input_path).read()

lines = raw.split("\n")

result = 0

for idx, line in enumerate(lines):
    expected = number_map
    first_digit = None
    last_digit = None

    for char in line:
        if char.isnumeric() is True:
            if first_digit is None:
                first_digit = int(char)
                continue
            last_digit = int(char)
        else:
            if char in expected.keys():
                if type(expected[char]) is int: 
                    if first_digit is None:
                        first_digit = expected[char]
                    else:
                        last_digit = expected[char]
                    
                    if char in number_map.keys():
                        temp = number_map[char]
                        expected = number_map 
                                    
                        expected = deep_update(char, number_map, number_map[char])  
                    else: 
                        expected = number_map  
                else: 
                    if char in number_map.keys():

                        expected = deep_update(char, number_map[char], expected[char])    
                    else: 
                        expected = expected[char]  
            else:
                if char in number_map.keys():
                    expected = number_map[char]
                else:
                    expected = number_map


    if first_digit:
        if last_digit: 
            result += first_digit*10 + last_digit
        else:
            result += first_digit*10+first_digit


print(result)