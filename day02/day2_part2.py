def main():
    data = open("input.txt", "r")
    data = [line.strip() for line in data]

    total = 0
    for line in data:
        _, info = line.split(": ")
        max_red, max_blue, max_green = 0, 0, 0

        for subset in info.split(";"):
            for cubes in subset.split(","):
                num_cubes = int(cubes.split()[0])
                if "red" in cubes: 
                    if num_cubes > max_red: max_red = num_cubes
                elif "blue" in cubes: 
                    if num_cubes > max_blue: max_blue = num_cubes
                elif "green" in cubes:
                    if num_cubes > max_green: max_green = num_cubes
        
        total += max_red * max_blue * max_green

    print(total)


if __name__ == "__main__":
    main()