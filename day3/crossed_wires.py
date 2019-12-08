# get wire segment / circuit information from input file
def get_wire_circuitry(fpath):
    with open(fpath, "r") as fp:
        wire1 = fp.readline().split(",")
        wire2 = fp.readline().split(",")
    return wire1, wire2

# traverse wire circuity, appending coordinate tuples to a list which gets returned as a set
def parse_wires(wc):
    coords = dict()
    curr = (0, 0)
    curr_step = 0
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
            curr_step += 1
            if curr not in coords.keys():
                coords[curr] = curr_step
    return coords

if __name__ == "__main__":
    
    # get all the coordinates of the wire circuitry for wire 1 and wire 2
    w1, w2 = get_wire_circuitry("input.txt")
    coords1 = parse_wires(w1)
    coords2 = parse_wires(w2)

    # get the set intersection of all the intersection coordinates
    set_int = list(set(coords1.keys()).intersection(set(coords2.keys())))

    # PART 1: compute manhattan distances from the origin and find min (cloest intersection)
    manhattan_dist = [abs(coord[0]) + abs(coord[1]) for coord in set_int]
    print(min(manhattan_dist))

    # PART 2: compute min combined number of steps out of all intersections
    step_sums = [coords1[coord] + coords2[coord] for coord in set_int]
    print(min(step_sums))
