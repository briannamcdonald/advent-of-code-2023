import re

def main():
    data = open("input.txt", "r")
    data = [line.strip() for line in data]

    total = 0
    for line in data:
        winning_nums_set, scratch_set = [set(num_list.split()) for num_list in re.sub("Card .*: ", "", line).split(" | ")]
        num_matches = len(winning_nums_set & scratch_set)
        if num_matches > 0:
            total += 2 ** (num_matches - 1)

    print(total)


if __name__ == "__main__":
    main()