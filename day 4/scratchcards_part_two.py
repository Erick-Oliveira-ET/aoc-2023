
from pathlib import WindowsPath

input_path = WindowsPath("." )/ "day 4" / "input.txt"

games = open(input_path).read().replace("Card ", "").split("\n")

points = 0

instances_arr = [1]*len(games)

for idx, card in enumerate(games):
    if len(card) == 0:
        break
    game_id, scores = card.split(":")
    
    winning_numbers, numbers_have = scores.split("|")

    winning_set = set([item for item in winning_numbers.split(" ") if item != ""])

    round_point_count = 0

    for num in numbers_have.split(" "):
        if num in winning_set and num != "":
            round_point_count += 1
    
    print(round_point_count)
    
    for instance_idx in range(idx+1,idx+1+round_point_count):
        instances_arr[instance_idx] += instances_arr[idx]
print(instances_arr)
points = sum(instances_arr)

print(points)