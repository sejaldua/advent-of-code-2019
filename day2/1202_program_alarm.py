def get_list(fpath):
    with open(fpath, "r") as fp:
        intcode = [int(num) for num in fp.read().split(",") if num != "\n"]
    return intcode

def init(intcode):
    intcode[1] = 12
    intcode[2] = 2
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

if __name__ == "__main__":
    intcode = get_list("input.txt")
    intcode = init(intcode)
    print(parse_ops(intcode))