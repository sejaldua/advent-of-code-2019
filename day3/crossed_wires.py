def get_wire_circuitry(fpath):
    with open(fpath, "r") as fp:
        wire1 = fp.readline().split(",")
        wire2 = fp.readline().split(",")
    return wire1, wire2

if __name__ == "__main__":
    w1, w2 = get_wire_circuitry("input.txt")
    print(w1, w2)
