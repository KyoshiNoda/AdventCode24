import re
f = open("day3/input.txt", "r")


def part1():
    file = f.read()
    valid_calls = re.findall("mul\(\d{1,3},\d{1,3}\)", file)
    result = 0
    for call in valid_calls:
        operation = re.findall("\d{1,3},\d{1,3}", call)[0]
        comma = operation.find(",")
        x = operation[:comma]
        y = operation[comma + 1:]

        result += int(x) * int(y)

    return result

def part2():
    pass


print(part1())
