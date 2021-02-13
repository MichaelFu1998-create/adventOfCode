from math import floor

# read in the puzzle
width = 31
puzzle = []
with open("puzzle_day3.txt", "r") as f:
    puzzle = f.read().splitlines()

all_line = ""

for line in puzzle:
    all_line += line

n = len(all_line)
height = floor(n / 31)
print("width: ", width, " | height: ", height)

# part 1
tree = 0
move_right = 1
current_pos = 0
x_count = 1
y_count = 0
# axis x + 1 means we need to move forward 1 or (31 * 11 - 11)
# axis y + 1 means we need to move forward 11 in all_line
while True:
    # move right
    if move_right % 4 != 0:
        if x_count % 31 == 0:
            current_pos -= 30
        else:
            current_pos += 1
        x_count += 1
    # move down
    else:
        current_pos += 31
        y_count += 1
        if y_count > height - 1:
            break
        if all_line[current_pos] == '#':
            tree += 1
    move_right += 1

print(tree)

# part 1


def count_tree(right, down):
    tree = 0
    move_right = 1
    current_pos = 0
    x_count = 1
    y_count = 0
    # axis x + 1 means we need to move forward 1 or (31 * 11 - 11)
    # axis y + 1 means we need to move forward 11 in all_line
    while True:
        # move right
        if move_right % (right + 1) != 0:
            if x_count % 31 == 0:
                current_pos -= 30
            else:
                current_pos += 1
            x_count += 1
        # move down
        else:
            current_pos += 31 * down
            y_count += 1 * down
            if y_count > height - 1:
                break
            if all_line[current_pos] == '#':
                tree += 1
        move_right += 1
    return tree


outcome = []
outcome.append(count_tree(1, 1))
outcome.append(count_tree(3, 1))
outcome.append(count_tree(5, 1))
outcome.append(count_tree(7, 1))
outcome.append(count_tree(1, 2))
result = 1
for n in outcome:
    result *= n
print(outcome)
print(result)
