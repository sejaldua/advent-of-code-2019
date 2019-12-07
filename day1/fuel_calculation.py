def quick_maths(fuel):
        return (fuel // 3) - 2

def calculate_fuel(fpath):
        total_fuel = 0
        with open(fpath, "r") as fp:
                num = int(fp.readline())
                while num:
                        total_fuel += quick_maths(num)
                        try:
                                num = int(fp.readline())
                        except:
                                break
        return total_fuel

if __name__ == "__main__":
    print(calculate_fuel("input.txt"))
