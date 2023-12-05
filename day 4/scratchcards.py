
from pathlib import WindowsPath

input_path = WindowsPath("." )/ "day 4" / "input.txt"

games = open(input_path).read().replace("Card ", "").split("\n")

points = 0

for card in games:
    if len(card) == 0:
        break
    game_id, scores = card.split(":")
    
    winning_numbers, numbers_have = scores.split("|")

    winning_set = set([item for item in winning_numbers.split(" ") if item != ""])

    round_point_count = 0

    for num in numbers_have.split(" "):
        if num in winning_set:
            round_point_count += 1
    
    if round_point_count > 0:
        points += 2**(round_point_count-1)

print(points)