import math
from pathlib import WindowsPath

input_path = WindowsPath("." )/ "Day 1" / "input.txt"

raw = open(input_path).read()

lines = raw.split("\n")

result = 0

first_digit = None
last_digit = None

for line in lines:
    first_digit = None
    last_digit = None

    for char in line:
        if char.isnumeric() is True:
            if first_digit is None:
                first_digit = int(char)
                continue
            last_digit = int(char)
    if first_digit:

        if last_digit: 
            result += first_digit*10 + last_digit
        else:
            result += first_digit*10+first_digit

    


print(result)