# parse input text file to get the range
def get_range(fpath):
    with open(fpath, "r") as fp:
        rng = [int(num) for num in fp.read().split("-")]
    return rng

# PART 1: increasing and at least one adjacent duplicate
def get_valid_passwords1(min, max):
    count = 0
    for num in range(min, max+1):
        l = [int(c) for c in str(num)]
        if all(l[i] <= l[i+1] for i in range(len(l)-1)) and any(l[i] == l[i+1] for i in range(len(l)-1)):
            count += 1
    return count

# function to account for all the edge cases when checking for consecutive duplicates
def check_for_duplicates(l):
    if l[0] == l[1] and l[1] != l[2]:
        return True
    elif any(l[i] != l[i+1] and l[i+1] == l[i+2] and l[i+2] != l[i+3] for i in range(len(l)-3)):
        return True
    elif l[3] != l[4] and l[4] == l[5]:
        return True
    else:
        return False

# PART 2: increasing and ONLY one adjacent duplicate
def get_valid_passwords2(min, max):
    count = 0
    for num in range(min, max+1):
        l = [int(c) for c in str(num)]
        if all(l[i] <= l[i+1] for i in range(len(l)-1)) and check_for_duplicates(l):
            count += 1
    return count

if __name__ == "__main__":
    rng = get_range("input.txt")
    print(get_valid_passwords1(rng[0], rng[1]))
    print(get_valid_passwords2(rng[0], rng[1]))