import re
filepath = "data/day1.txt"

def match_digit(line: str) -> int | None:
    digits:tuple = ("one", "two", "three", "four", "five", "six", 'seven', "eight", "nine")
    if digit := re.search("one|two|three|four|five|six|seven|eight|nine", line):
        return digits.index(digit[0]) + 1
    return None

def find_digit(line: str) -> int:
    ln:int = -1
    rn:int = -1
    for i in range(len(line)):
        ri = -(i + 1)
        if ln == -1:
            if line[i].isdigit():
                ln = int(line[i])
            else:
                if md := match_digit(line[:i+1]):
                    ln = md
        if rn == -1:
            if line[ri].isdigit():
                rn = int(line[ri])
            else:
                if rmd := match_digit(line[ri:]):
                    rn = rmd
        if ln != -1 and rn != -1:
            return 10 * ln + rn
    return 0


number = []
number2 = []
with open(filepath, mode = 'r') as file:
    for line in file.readlines():
        for i in line:
            if i.isdigit():
                ln = i
                break
        for i in line[::-1]:
            if i.isdigit():
                number.append(int(ln+i))
                break
        find_n = find_digit(line)
        print(f"{line.strip()}: {find_n}")
        number2.append(find_n)
print(sum(number2))

