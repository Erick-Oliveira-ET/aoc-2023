from pathlib import WindowsPath

input_path = WindowsPath("." )/ "day 3" / "input.txt"

raw = open(input_path).read().split("\n")

row_len = len(raw[0])

gear_box = "".join(raw)

memo = set()

def number_explorer(index, start_index = 0):
    if index in memo:
        return ""

    if index == (0, 0) or index < 0 or index > row_len*(int(start_index/row_len)+1)-1:
        return ""
    
    if not gear_box[index].isnumeric():
        return ""

    temp = gear_box[index]

    memo.add(index)

    temp = number_explorer(index - 1, start_index) + temp # left
    temp = temp + number_explorer(index + 1, start_index) # right

    return temp

gear_id_sum = 0

for idx, char in enumerate(gear_box):
    if not char.isnumeric() and char != ".":
        for idx_search in [idx-1, idx+1, idx-1+row_len, idx+row_len, idx+1+row_len, idx-1-row_len, idx-row_len, idx+1-row_len]:
            if idx_search not in memo and gear_box[idx_search].isnumeric():
                number = number_explorer(idx_search, idx_search)
                if number != "":
                    print(number)
                    gear_id_sum += int(number)

print(gear_id_sum)