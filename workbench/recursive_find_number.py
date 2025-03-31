line_matrix = ["...@...#...123", "...@...92...#", "..823...@...#"]


def find_number(line: str, i: int, n: int | None, p: int) -> int:
    if i >= len(line):
        return n if n is not None else -1
    if not line[i].isdigit():
        return find_number(line, i + 1, n, p)
    n = (n or 0) * 10 + int(line[i])
    return find_number(line, i + 1, n, p)


result = find_number(line_matrix[0], 0, None, 0)


print(find_number(line_matrix[1], 0, None, 0))
