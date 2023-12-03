import re

def main():
    data = open("input.txt", "r")
    data = [line.strip() for line in data]

    total = 0
    for i, line in enumerate(data):
        digits = re.finditer(r'\d+', line)

        for digit in digits:
            symbol_found = False

            for j in range(i - 1, i + 2):
                if j < 0 or j >= len(data): continue
                for k in range(digit.start() - 1, digit.end() + 1):
                    if k < 0 or k >= len(line): continue

                    if data[j][k] not in ".0123456789": 
                        symbol_found = True
                        break

            if symbol_found: total += int(digit.group())

    print(total)


if __name__ == "__main__":
    main()