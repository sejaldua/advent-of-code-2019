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

# the phase and input will be passed in as a list into the first argument of this function
def get_output(inputs, intcode):

    # instruction sizes for each op (first value in list is a dummy value)
    sizes = [0, 4, 4, 2, 2, 3, 3, 4, 4]
    idx = 0
    input_counter = 0
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
            # index into input list depending on how many input instructions have been completed
            intcode[intcode[idx+1]] = inputs[input_counter]
            input_counter += 1
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

def feed_amp_circuit(phases):
    output = 0
    for phase in phases:
        output = get_output([phase, output], intcode)
    return output

def permutation(input): 
    if len(input) == 0: 
        return [] 
    if len(input) == 1: 
        return [input] 
    l = []
    for i in range(len(input)): 
       m = input[i] 
       rem = input[:i] + input[i+1:] 
       for p in permutation(rem): 
           l.append([m] + p) 
    return l 

if __name__ == "__main__":

    # PART 1: tresting out every permutation of phase settings and finding max thrust output signal
    intcode = get_list("input.txt")
    perms = permutation([0, 1, 2, 3, 4])
    thrusts = [feed_amp_circuit(phases) for phases in perms]
    print(max(thrusts))