# arithmetic function for puzzle 1
def quick_maths1(fuel):
        return (fuel // 3) - 2

# recursive function for puzzle 2
def quick_maths2(fuel):
        if fuel < 9:
                return 0
        return (fuel // 3) - 2 + quick_maths2((fuel // 3) - 2)

# compute fuel needed for each input, then return the sum of these fuel requirements
def calculate_fuel(fpath):
        total_fuel = 0
        with open(fpath, "r") as fp:
                num = int(fp.readline())
                while num:
                        total_fuel += quick_maths2(num)
                        try:
                                num = int(fp.readline())
                        except:
                                break
        return total_fuel

if __name__ == "__main__":
    print(calculate_fuel("input.txt"))
