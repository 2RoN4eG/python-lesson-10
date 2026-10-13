
def read_lines(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.rstrip('\n') for line in f]


def write_lines(filename, lines):
    with open(filename, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + "\n")


def main():
    old_lines = read_lines("./Task 1/old.txt")
    # for index, line in enumerate(old_lines):
    #     print(f"o: {index}: {line}")
    # print()

    new_lines = read_lines("./Task 1/new.txt")
    # for index, line in enumerate(new_lines):
    #     print(f"n: {index}: {line}")
    # print()

    old = 0
    new = 0
    difference = []
    while old < len(old_lines) and new < len(new_lines):
        lhs = old_lines[old]
        rhs = new_lines[new]

        if lhs != rhs:
            if old + 1 < len(old_lines) and old_lines[old + 1] == new_lines[new]:
                # print(f"- old line is '{old_lines[o]}', new line is '{new_lines[n]}'")
                # print(f"- old line is '{old_lines[o + 1]}', new line is '{new_lines[n]}'")
                difference.append("-" + lhs)
                old += 1
            elif new + 1 < len(new_lines) and old_lines[old] == new_lines[new + 1]:
                # print(f"+ old line is '{old_lines[o]}', new line is '{new_lines[n]}'")
                # print(f"+ old line is '{old_lines[o]}', new line is '{new_lines[n + 1]}'")
                difference.append("+" + rhs)
                new += 1
            else:
                difference.append("-" + lhs)
                difference.append("+" + rhs)
                old += 1
                new += 1
        else:
            difference.append(rhs)
            old += 1
            new += 1

    # print(f"o is {o}, old file length is {len(old_lines)}")
    # print(f"n is {n}, new file length is {len(new_lines)}")

    while old < len(old_lines):
        lhs = old_lines[old]
        difference.append("-" + lhs)
        old += 1

    while new < len(new_lines):
        rhs = new_lines[new]
        difference.append("+" + rhs)
        new += 1

    # print()
    # for index, line in enumerate(difference):
    #     print(f"{index}: {line}")

    write_lines("./Task 1/diff.txt", difference)


if __name__ == "__main__":
    main()
