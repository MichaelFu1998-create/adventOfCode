import numpy as np
# read in the puzzle
with open("puzzle_day5.txt", "r") as f:
    puzzle = f.read().splitlines()

# part 1
seat_id = []
for boarding_pass in puzzle:
    row = np.arange(128)
    col = np.arange(8)
    for ch in boarding_pass:
        div_row = int(len(row) / 2)
        div_col = int(len(col) / 2)
        if ch == "F":
            row = row[:div_row]
        elif ch == "B":
            row = row[div_row:]
        elif ch == "R":
            col = col[div_col:]
        elif ch == "L":
            col = col[:div_col]
    id = row[0] * 8 + col[0]
    seat_id.append(id)
print(max(seat_id))

# part 2
from itertools import combinations 

arr = ["F", "B"]

lr = ["L", "R"]

list(combinations(arr, r)) 
for i in range(128):
    