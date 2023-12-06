from math import ceil, floor, sqrt
from pathlib import WindowsPath

input_path = WindowsPath("." )/ "day 6" / "input.txt"

raw = [row.split(":") for row in open(input_path).read().split("\n")]

time = [int(item.strip()) for item in raw[0][1].strip().split()]
record_distance = [int(item) for item in raw[1][1].strip().split()]

def y(b, x):
    return (b-x)*x

def bhaskara(a, b, c):
    return (-b + sqrt(b**2 - 4*a*c))/(2*a), (-b - sqrt(b**2 - 4*a*c))/(2*a)


product = 1

for available_time, rec_distance in zip(time, record_distance):
    x1, x2 = bhaskara(-1, available_time, -rec_distance)

    min_d = floor(x2)
    max_d = ceil(x1)
    
    if rec_distance == y(available_time, min_d):
        min_d -= 1
    if rec_distance == y(available_time, max_d):
        max_d += 1

    print("range", min_d - max_d + 1)

    product *= min_d - max_d + 1

print(product)

