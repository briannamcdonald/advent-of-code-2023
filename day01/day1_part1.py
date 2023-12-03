def main():
    data = open("input.txt", "r")
    data = [line.strip() for line in data]

    total = 0
    for line in data:
        first = ""
        last = ""

        for char in line:
            if char.isdigit():
                if first == "": first += char
                else: last = char

        if last != "":
            total += int(first + last)
        else:
            total += int(first * 2)

    print(total)


if __name__ == "__main__":
    main()