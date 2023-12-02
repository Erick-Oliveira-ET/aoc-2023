import math
from pathlib import WindowsPath

input_path = WindowsPath("." )/ "day 2" / "input.txt"

games = open(input_path).read().replace("Game ", "").split("\n")

possibility = {
    "blue": 14,
    "red" : 12,
    "green": 13
}
# possibility = {
#     "blue": 14,
#     "red" : 12,
#     "green": 13
# }

id_sum = 0

for game in games:
    if len(game) == 0:
        break
    game_id, scores = game.split(":")
    
    score_board = scores.split(";")

    not_possible = False

    for score_round in score_board:
        if not_possible:
            break

        color_count = score_round.split(",")

        for color_score_str in color_count:
            qnt, color = color_score_str.removeprefix(" ").split(" ")
            
            if int(qnt) > possibility[color]:
                not_possible = True
                break
        
    if not not_possible:
        id_sum += int(game_id)    

print(id_sum)

