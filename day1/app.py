import heapq
file = open("day1/input.txt", "r")


def part1():
    heap1, heap2 = [], []
    size = 0
    for line in file:
        x, y = line.split()
        heap1.append(x)
        heap2.append(y)
        size += 1

    heapq.heapify(heap1)
    heapq.heapify(heap2)

    result = 0
    while size > 0:
        e1, e2 = heapq.heappop(heap1), heapq.heappop(heap2)
        result += abs(int(e1) - int(e2))
        size -= 1

    return result


def part2():
    values, freq = [], {}
    for line in file:
        x, y = line.split()
        values.append(x)
        freq[y] = freq.get(y, 0) + 1
    result = 0
    for value in values:
        result += int(value) * int(freq.get(value, 0))
    return result

