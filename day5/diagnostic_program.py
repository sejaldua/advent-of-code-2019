def get_list(fpath):
    intcode = [int(num) for num in open(fpath, "r").read().split(",")]
    return intcode

# --- THE OPCODES ---
# 1: add
# 2: multiply
# 3: input
# 4: output
# 5: jump-if-true
# 6: jump-if-false
# 7: less than
# 8: equals

def parse_ops(input, intcode):
    # instruction sizes for each op (first value in list is a dummy value)
    sizes = [0, 4, 4, 2, 2, 3, 3, 4, 4]
    idx = 0
    op = intcode[idx]

    # loop until halt
    while op != 99:

        # parse modes using modulo division
        modes = [(op // 10 ** i) % 10 for i in range(2, 5)]
        op = op % 100

        # get params
        num_elems = sizes[op]
        args = [intcode[idx + i] for i in range(1, num_elems)]
        params = [x if modes[i] else intcode[x] for i, x in enumerate(args)]

        # execute instructions
        if op == 1:
            intcode[args[2]] = params[0] + params[1]
        elif op == 2:
            intcode[args[2]] = params[0] * params[1]
        elif op == 3:
            intcode[args[0]] = input
        elif op == 4:
            output = params[0]
        elif op == 5:
            if params[0]:
                idx = params[1]
                op = intcode[idx]
                continue
        elif op == 6:
            if not params[0]:
                idx = params[1]
                op = intcode[idx]
                continue
        elif op == 7:
            intcode[args[2]] = int(params[0] < params[1])
        elif op == 8:
            intcode[args[2]] = int(params[0] == params[1])

        # get new op
        idx += num_elems
        op = intcode[idx]

    # return output after halt
    return output

if __name__ == "__main__":

    # PART 1: diagnostic code for system ID 1
    intcode = get_list("input.txt")
    print(parse_ops(1, intcode))

    # PART 2: diagnostic code for systme ID 5 (with 4 new opcodes)
    intcode = get_list("input.txt")
    print(parse_ops(5, intcode))