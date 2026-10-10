print("new text")


def read_lines(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.rstrip('\n') for line in f]


def main():
    old_lines = read_lines("./Task 1/old.txt")
    # for index, line in enumerate(old_lines):
    #     print(f"o: {index}: {line}")
    # print()

    new_lines = read_lines("./Task 1/new.txt")
    # for index, line in enumerate(new_lines):
    #     print(f"n: {index}: {line}")
    # print()

    o = 0
    n = 0
    difference = []
    while o < len(old_lines) and n < len(new_lines):
        lhs = old_lines[o]
        rhs = new_lines[n]

        if lhs != rhs:
            if o + 1 < len(old_lines) and old_lines[o + 1] == new_lines[n]:
                # print(f"- old line is '{old_lines[o]}', new line is '{new_lines[n]}'")
                # print(f"- old line is '{old_lines[o + 1]}', new line is '{new_lines[n]}'")
                difference.append("- " + lhs)
                o += 1
            elif n + 1 < len(new_lines) and old_lines[o] == new_lines[n + 1]:
                # print(f"+ old line is '{old_lines[o]}', new line is '{new_lines[n]}'")
                # print(f"+ old line is '{old_lines[o]}', new line is '{new_lines[n + 1]}'")
                difference.append("+ " + rhs)
                n += 1
            else:
                difference.append("- " + lhs)
                difference.append("+ " + rhs)

                o += 1
                n += 1
        else:
            difference.append(lhs)
            o += 1
            n += 1

    # print(f"o is {o}, old file length is {len(old_lines)}")
    # print(f"n is {n}, new file length is {len(new_lines)}")

    while o < len(old_lines):
        lhs = old_lines[o]
        difference.append("- " + lhs)
        o += 1

    while n < len(new_lines):
        rhs = new_lines[n]
        difference.append("+ " + rhs)
        n += 1

    print()
    for index, line in enumerate(difference):
        print(f"{index}: {line}")


if __name__ == "__main__":
    main()
