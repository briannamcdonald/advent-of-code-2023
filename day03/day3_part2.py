import re

def main():
    data = open("input.txt", "r")
    data = [line.strip() for line in data]

    total = 0
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if char == "*":
                adj_nums = []

                for k in range(i - 1, i + 2):
                    if k < 0 or k >= len(data): continue
                    digits = re.finditer(r'\d+', data[k])

                    for digit in digits:
                        for l in range(j - 1, j + 2):
                            if l < 0 or l >= len(line): continue

                            if data[k][l].isdigit() and l >= digit.start() and l <= digit.end():
                                adj_nums.append(int(digit.group()))
                                break

                if len(adj_nums) == 2: total += adj_nums[0] * adj_nums[1]

    print(total)


if __name__ == "__main__":
    main()