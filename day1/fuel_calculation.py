# arithmetic function for puzzle 1
def quick_maths1(fuel):
    return (fuel // 3) - 2

# recursive function for puzzle 2
def quick_maths2(fuel):
    f = quick_maths1(fuel)
    return 0 if f <= 0 else f + quick_maths2(f)

# aggregate fuel requirements for each module based on input mass and fuel equation
def calculate_fuel(fpath, puzzle_func):
    return sum(puzzle_func(int(mass)) for mass in open(fpath, 'r'))

if __name__ == "__main__":
    print(calculate_fuel("input.txt", quick_maths1))
    print(calculate_fuel("input.txt", quick_maths2))
