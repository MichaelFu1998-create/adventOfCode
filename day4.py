import re

# read in the puzzle
with open("puzzle_day4.txt", "r") as f:
    puzzle = f.read().splitlines()

# part 1 + 2
passport = []
one_passport = ""

for line in puzzle:
    if len(line) != 0:
        one_passport += (" " + line)
    else:
        passport.append(one_passport)
        one_passport = ""

legal_ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
valid = 0

for p in passport:
    is_valid = True
    data = p.strip(" ").split(" ")
    if len(data) < 7:
        continue
    if len(data) == 7:
        no_cid = True
        for field in data:
            field = field.split(":")[0]
            if field == "cid":
                no_cid = False
        if no_cid == False:
            continue
    if len(data) == 8 or len(data) == 7:
        for field in data:
            key = field.split(":")[0]
            value = field.split(":")[1]            
            if key == "byr":
                if int(value) < 1920 or int(value) > 2002:
                    is_valid = False
                    break
            elif key == "iyr":
                if int(value) < 2010 or int(value) > 2020:
                    is_valid = False
                    break
            elif key == "eyr":
                if int(value) < 2020 or int(value) > 2030:
                    is_valid = False
                    break               
            elif key == "hgt":
                if value[-2:] == "cm":
                    if int(value[:-2]) < 150 or int(value[:-2]) > 193:
                        is_valid = False
                        break
                elif value[-2:] == "in":
                    if int(value[:-2]) < 59 or int(value[:-2]) > 76:
                        is_valid = False
                        break
                else:
                    is_valid = False
                    break      
            elif key == "hcl":
                if len(value) != 7:
                    is_valid = False
                    break
                x = re.search("^#[a-f0-9]", value)
                if x == None:
                    is_valid = False
                    break
            elif key == "ecl":
                if value not in legal_ecl:
                    is_valid = False
                    break
            elif key == "pid":
                if len(value) != 9:
                    is_valid = False
                    break
                if re.search("[0-9]", value) == None:
                    is_valid = False
                    break
    if is_valid:
        valid += 1    

print(valid)