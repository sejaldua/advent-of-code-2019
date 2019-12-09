def get_list(fpath):
    with open(fpath, "r") as fp:
        intcode = [int(num) for num in fp.read().split(",") if num != "\n"]
    return intcode

def init(intcode, noun, verb):
    intcode[1] = noun
    intcode[2] = verb
    return intcode

def parse_ops(intcode):
    for i in range(len(intcode) // 4):
        idx = i*4
        if intcode[idx] == 1:
            intcode[intcode[idx + 3]] = intcode[intcode[idx + 1]] + intcode[intcode[idx + 2]]
        elif intcode[idx] == 2:
            intcode[intcode[idx + 3]] = intcode[intcode[idx + 1]] * intcode[intcode[idx + 2]]
        elif intcode[idx] == 99:
            return intcode[0]
        else:
            print("something went wrong. op is", intcode[idx])

def run():
    for noun in range(1, 100):
        for verb in range(1, 100):
            intcode = get_list("input.txt")
            intcode = init(intcode, noun, verb)
            if parse_ops(intcode) == 19690720:
                return 100 * noun + verb
            else:
                #print("not it", noun, verb)
                pass

if __name__ == "__main__":

    # PART 1: value at position 0 after program halts
    intcode = get_list("input.txt")
    intcode = init(intcode, 12, 2)
    print(parse_ops(intcode))

    # PART 2: input noun and verb that cause the program to produce output 19690720
    print(run())