file = open("day2/sample.txt", "r")


def part1():
    """
    - safe reports:
        - monotonic increasing/decreasing
        - difference between each number in level, is between 1-3
    - return amount of safe reports
    """
    safe_reports = 0

    for level in file:
        level_list = [int(n) for n in level.split()]
        left = 0
        safe_flag = True

        # mono increasing
        if level_list[1] > level_list[0]:
            for right in range(1, len(level_list)):
                if (
                    level_list[left] >= level_list[right] or
                    not (1 <= abs(level_list[left] - level_list[right]) <= 3)
                ):
                    safe_flag = False
                    break
                left += 1

        # mono decreasing
        else:
            for right in range(1, len(level_list)):
                if (
                    level_list[left] <= level_list[right] or
                    not (1 <= abs(level_list[left] - level_list[right]) <= 3)
                ):
                    safe_flag = False
                    break
                left += 1

        if safe_flag:
            safe_reports += 1

    return safe_reports


def part2():
    """
    Same as before, only permit ONE bad report.
    """
    safe_reports = 0

    def is_safe_report(level_list):
        mono_increase = all(
            level_list[i] < level_list[i + 1] and
            1 <= abs(level_list[i] - level_list[i + 1]) <= 3

            for i in range(len(level_list) - 1)
        )
        mono_decrease = all(
            level_list[i] > level_list[i + 1] 
            and 1 <= abs(level_list[i] - level_list[i + 1]) <= 3

            for i in range(len(level_list) - 1)
        )

        return mono_increase or mono_decrease

    for level in file:
        level_list = [int(n) for n in level.split()]

        if is_safe_report(level_list):
            safe_reports += 1
            continue

        safe_with_removal = False
        for i in range(len(level_list)):
            modified_list = level_list[:i] + level_list[i + 1:]
            if is_safe_report(modified_list):
                safe_with_removal = True
                break

        if safe_with_removal:
            safe_reports += 1

    return safe_reports