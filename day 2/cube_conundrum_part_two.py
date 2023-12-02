import math
from pathlib import WindowsPath

input_path = WindowsPath("." )/ "day 2" / "input.txt"

games = open(input_path).read().replace("Game ", "").split("\n")

power_sum = 0

for game in games:
    if len(game) == 0:
        break
    game_id, scores = game.split(":")
    
    score_board = scores.split(";")

    not_possible = False

    min_req = {
    "blue": 0,
    "red" : 0,
    "green": 0
}

    for score_round in score_board:
        color_count = score_round.split(",")

        for color_score_str in color_count:
            qnt, color = color_score_str.removeprefix(" ").split(" ")
            
            if int(qnt) > min_req[color]:
                min_req[color] = int(qnt)
    
    temp = 1

    for value in min_req.values():
        temp *= value

    power_sum += temp

print(power_sum)

