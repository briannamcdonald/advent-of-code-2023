def main():
    data = open("input.txt", "r")
    data = [line.strip() for line in data]

    MAX_RED, MAX_BLUE, MAX_GREEN = 12, 14, 13

    total = 0
    for line in data:
        game_id, info = line.split(": ")
        
        possible = True
        for subset in info.split(";"):
            for cubes in subset.split(","):
                if "red" in cubes: max_val = MAX_RED
                elif "blue" in cubes: max_val = MAX_BLUE
                elif "green" in cubes: max_val = MAX_GREEN

                if int(cubes.split()[0]) > max_val:
                    possible = False
                    break

            if not possible: break
        
        if possible: total += int(game_id.split()[1])

    print(total)


if __name__ == "__main__":
    main()