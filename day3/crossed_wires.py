# get wire segment / circuit information from input file
def get_wire_circuitry(fpath):
    with open(fpath, "r") as fp:
        wire1 = fp.readline().split(",")
        wire2 = fp.readline().split(",")
    return wire1, wire2

# traverse wire circuity, appending coordinate tuples to a list which gets returned as a set
def parse_wires(wc):
    coords = []
    curr = (0, 0)
    for wire in wc:
        for _ in range(int(wire[1:])):
            if wire[0] == "D":
                curr = (curr[0] - 1, curr[1])
            elif wire[0] == "U":
                curr = (curr[0] + 1, curr[1])
            elif wire[0] == "L":
                curr = (curr[0], curr[1] - 1)
            elif wire[0] == "R":
                curr = (curr[0], curr[1] + 1)
            else:
                print("something is wrong")
            coords.append(curr)
    return set(coords)

if __name__ == "__main__":
    
    # get all the coordinates of the wire circuitry for wire 1 and wire 2
    w1, w2 = get_wire_circuitry("input.txt")
    coords1 = parse_wires(w1)
    coords2 = parse_wires(w2)

    # get the set intersection of all the intersection coordinates
    set_int = list(coords1.intersection(coords2))

    # compute manhattan distances from the origin
    manhattan_dist = []
    for coord in set_int:
        manhattan_dist.append(abs(coord[0]) + abs(coord[1]))

    # closest intersection: print(set_int[manhattan_dist.index(min(manhattan_dist))])
    print(min(manhattan_dist))
    

