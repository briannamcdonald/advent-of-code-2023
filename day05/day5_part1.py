def main():
    data = open("input.txt", "r")
    data = [line.strip() for line in data]

    # dict where the key is an index and the value is a tuple with the seed value and a boolean representing if the value has already been mapped for the current map
    seed_dict = {i: (int(s), False) for i, s in enumerate(data[0].replace("seeds: ", "").split())}
    
    for line in data:
        if line == "" or "seeds:" in line: continue
        elif "map" in line: 
            # reset the boolean values for the new map
            seed_dict = {i: (s, False) for i, (s, _) in seed_dict.items()}
            continue

        dest_range_start, source_range_start, range_len = [int(val) for val in line.split()]

        for i, (seed, already_mapped) in seed_dict.items():
            if seed >= source_range_start and seed < source_range_start + range_len and not already_mapped:
                new_val = dest_range_start + (seed - source_range_start)
                seed_dict[i] = (new_val, True)

    print(min(seed_dict.values())[0])


if __name__ == "__main__":
    main()