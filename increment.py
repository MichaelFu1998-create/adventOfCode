# deck_size - 1 = 9, increment = 3
# 0 1 2 3 4 5 6 7 8 9
# 0 . . 1 . . 2 . . 3
# 0 . 4 1 . 5 2 . 6 3
# 0 7 4 1 8 5 2 9 6 3

# segment 1
# 7 4 1
# segment 2
# 8 5 2
# segment 3
# 9 6 3

####################################################

# deck_size - 1 = 8, increment = 4
# 0 1 2 3 4 5 6 7 8
# 0 . . . 1 . . . 2
# 0 . . 3 1 . . 4 2
# 0 . 5 3 1 . 6 4 2
# 0 7 5 3 1 8 6 4 2

# segment 1
# 7 5 3 1
# segment 2
# 8 6 4 2

####################################################

# deck_size - 1 = 10, increment = 5
# 0 1 2 3 4 5 6 7 8 9 10
# 0 . . . . 1 . . . . 2
# 0 . . . 3 1 . . . 4 2
# 0 . . 5 3 1 . . 6 4 2
# 0 . 7 5 3 1 . 8 6 4 2
# 0 9 7 5 3 1 10 8 6 4 2

# segment 1
# 9 7 5 3 1
# segment 2
# 10 8 6 4 2

# if (deck_size - 1) % increment == 0
# then the rule above will appear
# num of segment = (deck_size - 1) / increment

########################################################################################################

# deck_size - 1 = 9, increment = 4
# (deck_size - 1) % increment = 1
# 0 1 2 3 4 5 6 7 8 9
# 0 . . . 1 . . . 2 . R1
# 0 . 3 . 1 . 4 . 2 . R2
# 0 5 3 . 1 6 4 . 2 7 R3 (CONFLICT 0)
# 0 5 3 8 1 6 4 9 2 7 R4

# should be able to compute how many times we cross the boundary, which is also (round - 1)

# compute the index for each number

###R1###
# number 1 >> 4(increment) * 1(original index) - 9(deck_size-1) * 0(round - 1) - (round - 1) = 4
# number 2 >> 4 * 2 - 9 * 0 = 8

###R2###
# number 3 >> 4 * 3 - 9 * 1 - 1 = 2
# number 4 >> 4 * 4 - 9 * 1 - 1 = 6

###R3###
# number 5 >> 4 * 5 - 9 * 2 - 2 = 0 + 1 = 1 (( 0 is already occupied >> therefore + 1
# number 6 >> 4 * 6 - 9 * 2 - 2 = 4 + 1 = 5
# number 7 >> 4 * 7 - 9 * 2 - 2 = 8 + 1 = 9

###R4###
# number 8 >> 4 * 8 - 9 * 3 - 3 = 2 >> + 1 = 3
# number 9 >> 4 * 9 - 9 * 3 - 3 = 6 >> + 1 = 7

####################################################

# deck_size - 1 = 9, increment = 7
# (deck_size - 1) % increment = 2
# 0 1 2 3 4 5 6 7 8 9
# 0 . . . . . . 1 . . R1
# 0 . . . 2 . . 1 . . R2
# 0 3 . . 2 . . 1 . . R3
# 0 3 . . 2 . . 1 4 . R4
# 0 3 . . 2 5 . 1 4 . R5
# 0 3 6 . 2 5 . 1 4 7 R6
# 0 3 6 . 2 5 8 1 4 7 R7
# 0 3 6 9 2 5 8 1 4 7 R8

####################################################

# deck_size - 1 = 9, increment = 6
# (deck_size - 1) % increment = 3
# 0 1 2 3 4 5 6 7 8 9
# 0 . . . . . 1 . . . R1
# 0 . 2 . . . 1 . 3 . R2
# 0 . 2 . 4 . 1 . 3 . R3
# 0 5 2 . 4 . 1 6 3 . R4 (5 CONFLICT 0)
# 0 3 2 7 4 . 1 6 3 8 R5
# 0 3 2 7 4 9 1 6 3 8 R6

# 15 % 6 = 3
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# 0 . . . . . 1 . . . .  .  2  .  .  .  R1
# 0 . 3 . . . 1 . 4 . .  .  2  .  5  .  R2
# 0 . 3 . 6 . 1 . 4 . 7  .  2  .  5  .  R3
# 0 8 3 . 6 . 1 9 4 . 7  .  2  10 5  .  R4 (8 CONFLICT 0)
# 0 8 3 11 6 . 1 9 4 12 7 . 2 10 5 13   R5
# 0 8 3 11 6 14 1 9 4 12 7 15 2 10 5 13 R6

# 4(increment) * 1(original index) - 9(deck_size-1) * 0(round - 1) - (round - 1) = 4
# number 5 >> 6 * 5 - 9 * 3 - 3 = 0 + 1 = 1
# number 9 >> 6 * 9 - 9 * 5 - 5 = 4 + 1 = 5

####################################################
# deck_size - 1 = 9, increment = 5
# (deck_size - 1) % increment = 4
# 0 1 2 3 4 5 6 7 8 9
# 0 . . . . 1 . . . . R1
# 0 2 . . . 1 3 . . . R2 (2 CONFLICT 0)
# 0 2 4 . . 1 3 5 . . R3 (4 CONFLICT 2)
# 0 2 4 6 . 1 3 5 7 . R4 (6 CONFLICT 4)
# 0 2 4 6 8 1 3 5 7 9 R5 (8 CONFLICT 6)

# number 9 >> 4 conflict >>

# we need to compute the round and the conflict...
# the formula to compute the new index is as below
################################################################################################################

### (increment) * (original index) - (deck_size-1) * (round - 1) - (round - 1) + num_of_conflict = new_index ###
# Note. num_of_conflict = 0 when (deck_size - 1) % increment = 0

################################################################################################################


####################### compute Round given the original index, increment, and deck_size #######################
# total distance the original index is supposed to move = (increment) * (original index)
# floor(((increment) * (original index)) / deck_size) + 1(Round starts from 1) = Round
################################################################################################################


# how to compute the num_of_conflict given the Round ???
