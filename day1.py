# read in the puzzle
puzzle = []
with open("puzzle_day1.txt", "r") as f:
    for line in f:
        puzzle.append(int(line.rstrip('\n')))

# part 1
max_index = len(puzzle) - 1
for i in range(max_index):
    for j in range(i+1, max_index):
        if (puzzle[i] + puzzle[j] == 2020):
            print(puzzle[i] * puzzle[j])

# part 2
for i in range(max_index):
    for j in range(i+1, max_index):
        for k in range(j+1, max_index):
            if (puzzle[i] + puzzle[j] + puzzle[k] == 2020):
                print(puzzle[i] * puzzle[j] * puzzle[k])
