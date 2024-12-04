file = open("day4/sample.txt", "r")


def part1():
    # build grid
    grid = []
    for line in file:
        row = []
        for col in line[:-1]:
            row.append(col)
        grid.append(row)

    ROWS, COLS = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),  # horizontal/vertical
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]  # diagonal
    target = "XMAS"

    def dfs(row, col, index, visited):
        if index == len(target):
            return True
        if (
            row < 0 or col < 0 or
            row >= ROWS or col >= COLS or
            (row, col) in visited or
            grid[row][col] != target[index]
        ):
            return False

        visited.add((row, col))
        for dr, dc in directions:
            if dfs(row + dr, col + dc, index + 1, visited):
                return True
        visited.remove((row, col))
        return False

    result = 0
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == target[0]:
                visited = set()
                if dfs(row, col, 0, visited):
                    result += 1
    return result


def part2():
    pass


part1()
