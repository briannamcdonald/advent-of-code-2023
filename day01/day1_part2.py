def main():
    data = open("input.txt", "r")
    data = [line.strip() for line in data]

    digits = {
        "one": "1", 
        "two": "2", 
        "three": "3", 
        "four": "4", 
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    total = 0
    for line in data:
        first = ""
        last = ""

        for i, char in enumerate(line):
            if char.isdigit():
                if first == "": first += char
                else: last = char
            
            else:
                for k, v in digits.items():
                    if i + len(k) > len(line): continue
                    else: 
                        if k == line[i : i + len(k)]:
                            if first == "": first += v
                            else: last = v

        if last != "":
            total += int(first + last)
        else:
            total += int(first * 2)

    print(total)


if __name__ == "__main__":
    main()