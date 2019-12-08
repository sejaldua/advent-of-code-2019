def get_range(fpath):
    with open(fpath, "r") as fp:
        rng = [int(num) for num in fp.read().split("-")]
    return rng

def get_valid_passwords(min, max):
    count = 0
    for num in range(min, max+1):
        l = [int(c) for c in str(num)]
        if all(l[i] <= l[i+1] for i in range(len(l)-1)) and any(l[i] == l[i+1] for i in range(len(l)-1)):
            count += 1
    return count

if __name__ == "__main__":
    rng = get_range("input.txt")
    print(get_valid_passwords(rng[0], rng[1]))