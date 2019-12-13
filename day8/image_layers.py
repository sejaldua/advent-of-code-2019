def solve_part_1(img, width, height):
    layer_sizes = [width * height * i for i in range(int(len(img) / (width * height)))]
    min_zeroes = int(len(img) / height)
    temp_answer = 0
    for i in range(len(layer_sizes)-1):
        curr_layer_counts = [0, 0, 0]
        for char in img[layer_sizes[i]:layer_sizes[i+1]]:
            curr_layer_counts[int(char)] += 1
        if curr_layer_counts[0] <= min_zeroes:
            min_zeroes = curr_layer_counts[0]
            temp_answer = curr_layer_counts[1] * curr_layer_counts[2]
    return temp_answer

if __name__ == "__main__":
    img = open('input.txt', 'r').read()[:-1]
    print(solve_part_1(img, 25, 6))