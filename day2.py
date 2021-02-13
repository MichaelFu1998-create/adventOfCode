# read in the puzzle
puzzle = []
with open("puzzle_day2.txt", "r") as f:
    for line in f:
        puzzle.append(line.rstrip('\n'))

# part 1
valid = 0

for block in puzzle:
    policy_pwd = block.split(":")
    policy = policy_pwd[0]
    pwd = policy_pwd[1]

    valid_number = policy.split(' ')[0]
    mini = int(valid_number.split('-')[0])
    maxi = int(valid_number.split('-')[1])

    char = policy.split(' ')[1]

    count = 0
    for c in pwd:
        if (c == char):
            count += 1
    if (mini <= count <= maxi):
        valid += 1
print(valid)

# part 2
valid = 0

for block in puzzle:
    policy_pwd = block.split(":")
    policy = policy_pwd[0]
    pwd = policy_pwd[1]
    pwd = pwd.strip(' ')
    valid_number = policy.split(' ')[0]
    pos_a = int(valid_number.split('-')[0])
    pos_b = int(valid_number.split('-')[1])

    char = policy.split(' ')[1]

    index = 0
    count = 0
    for c in pwd:
        if c == char and ((index + 1) == pos_a or (index + 1) == pos_b):
            count += 1
        index += 1
    if count == 1:
        valid += 1

print(valid)
