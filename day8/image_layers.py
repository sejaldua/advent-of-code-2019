from collections import defaultdict

def get_layers(img, width, height):
    layers = defaultdict(list)
    layer_sizes = [width * height * i for i in range(int(len(img) / (width * height) + 1))]
    layer = 0
    for i in range(len(layer_sizes)-1):
        for char in img[layer_sizes[i]:layer_sizes[i+1]]:
            layers[layer].append(int(char))
        layer += 1
    return layers

def print_image(layers, width, height):
    for y in range(height):
        for x in range(width):
            idx = x + y * width
            for l in range(len(layers)):
                # transparent pixel
                if layers[l][idx] == 2:
                    continue
                # white pixel
                elif layers[l][idx] == 1:
                    print("*", end="")
                # black pixel
                else:
                    print(" ", end="")
                break
        print()

if __name__ == "__main__":

    # read image from input file and extract layers
    img = open('input.txt', 'r').read()[:-1]
    width = 25
    height = 6
    layers = get_layers(img, width, height)

    # PART 1: find layer with fewest zeroes and return number of 1s * number of 2s
    zero_counts  = [pixels.count(0) for pixels in layers.values()]
    result_layer = zero_counts.index(min(zero_counts))
    print(layers[result_layer].count(1) * layers[result_layer].count(2))

    # PART 2: decode message
    print_image(layers, width, height)