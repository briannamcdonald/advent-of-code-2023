import re

def main():
    data = open("input.txt", "r")
    data = [line.strip() for line in data]

    # originally assume there is 1 copy of each card
    num_copies = {i: 1 for i in range(len(data))}

    for i, line in enumerate(data):
        winning_nums_set, scratch_set = [set(num_list.split()) for num_list in re.sub("Card .*: ", "", line).split(" | ")]
        num_matches = len(winning_nums_set & scratch_set)
        for j in range(1, num_matches + 1):
            num_copies[i + j] += num_copies[i]
    
    total = sum(n for n in num_copies.values())
    print(total)


if __name__ == "__main__":
    main()