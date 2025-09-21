import sys
import copy
import ex5_helper
import math

#################################################################
# FILE : cartoonify.py
# WRITER : Tomer Titinger , tomer.titinger , 208611939
# EXERCISE : intro2cs2 ex5 2021
# DESCRIPTION: Program the does several image processing functions,
# getting a picture and returns a "cartooned" version of it
#
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED: https://setosa.io/ev/image-kernels/
# NOTES: ...
#################################################################

def separate_channels(image):
    '''Function that gets a multicolored image,
    returns a list of one colored images'''
    image_rows = len(image)
    image_columns = len(image[0])
    image_channels = len(image[0][0])
    separated_image = []
    for channel in range(image_channels):
        separated_image.append([])
        for row in range(image_rows):
            separated_image[channel].append([])
            for column in range(image_columns):
                separated_image[channel][row].\
                    append(image[row][column][channel])
    return separated_image


def combine_channels(channels):
    '''Function that gets a list of one colored images,
    returns a one multicolored images'''
    channels_len = len(channels)
    rows_len = len(channels[0])
    columns_len = len(channels[0][0])
    combined_image = []
    for row in range(rows_len):
        combined_image.append([])
        for column in range(columns_len):
            combined_image[row].append([])
            for channel in range(channels_len):
                combined_image[row][column].\
                    append(channels[channel][row][column])
    return combined_image


def RGB2grayscale(colored_image):
    '''Function that gets a colored image, returns a
    grayscale version of it'''
    colored_rows = len(colored_image)
    colored_column = len(colored_image[0])
    updated_image = []
    for row in range(colored_rows):
        updated_image.append([])
        for column in range(colored_column):
            updated_image[row].append([])
            graychannel = (colored_image[row][column][0] * 0.299)\
                          + (colored_image[row][column][1] * 0.587)\
                          + (colored_image[row][column][2] * 0.114)
            updated_image[row][column] = round(graychannel)
    return updated_image


def blur_kernel(size):
    '''Function that gets a size of the wanted kernel,
    and returns that kernel'''
    blur_list = []
    for index in range(size):
        blur_list.append([])
        for iteration in range(size):
            blur_list[index].append(1/ (size ** 2))
    return blur_list


def apply_kernel(image, kernel):
    '''Funcion that gets an image and applies the kernel on the image,
    blurring pixels as set in blur_kernel '''
    ker_limits = len(kernel) // 2
    image_rows = len(image)
    image_columns = len(image[0])
    new_image = copy.deepcopy(image)

    for row in range(image_rows):
        for column in range(image_columns):
            sum = 0
            for row_ker in range(len(kernel)):
                for col_ker in range(len(kernel)):
                    image_row = (row - ker_limits) + row_ker
                    image_col = (column - ker_limits) + col_ker
                    if image_row >= image_rows or image_row < 0 or \
                            image_col >= image_columns or image_col < 0:
                        sum += kernel[row_ker][col_ker] * image[row][column]
                    else:
                        sum += kernel[row_ker][col_ker] *\
                               image[image_row][image_col]
            new_image[row][column] = round(sum)
    return new_image


def bilinear_interpolation(image, y, x):
    ''' Function that gets an image with specific coordinates
    of a pixel, returns a new value of the pixel according to
    the given formula in the exercise'''
    low_x = math.floor(x)
    high_x = math.ceil(x)
    low_y = math.floor(y)
    high_y = math.ceil(y)
    a = image[low_y][low_x]
    b = image[high_y][low_x]
    c = image[low_y][high_x]
    d = image[high_y][high_x]
    x = x - low_x
    y = y - low_y
    pixel_value = round(a * (1 - x) * (1 - y) + b * y * (1 - x)
                        + c * x *(1 - y) + d * (x*y))
    return pixel_value


def resize(image, new_height, new_width):
    '''Function that gets an image new height and width,
     returns a new image, in new height and new width'''
    new_image = []
    old_height = len(image)
    old_width = len(image[0])
    best_y = (old_height - 1) / (new_height - 1)
    best_x = (old_width - 1) / (new_width - 1)
    for row in range(new_height):
        new_image.append([])
        for column in range(new_width):
            new_image[row].append(0)

    for y in range(new_height):
        for x in range(new_width):
            new_image[y][x] = (bilinear_interpolation(image, y*best_y,
                                                      x*best_x))
    return new_image


def rotate_90(image, direction):
    '''Function that rotates the image 90 degrees
    to given direction, R for right, L for left'''
    rotated = []
    if direction == "R":
        for row in range(len(image[0])):
            rotated.append([])
            for column in range(len(image)):
                rotated[row].append(image[len(image) - 1 - column][row])
        return rotated

    if direction == "L":
        for row in range(len(image[0])):
            rotated.append([])
            for column in range(len(image)):
                rotated[row].append(image[column][len(image[0]) - 1 - row])
        return rotated


def get_edges(image, blur_size, block_size, c):
    '''Function that gets a one colored image, blur size, block size and a
     number, returns a new image when edges of the image are black'''
    blurred_image = apply_kernel(image, blur_kernel(blur_size))
    threshold_image = apply_kernel(blurred_image, blur_kernel(block_size))
    new_image = []
    for row in range(len(image)):
        new_image.append([])
        for column in range(len(image[0])):
            if blurred_image[row][column] < threshold_image[row][column] - c:
                new_image[row].append(0)
            else:
                new_image[row].append(255)
    return new_image


def quantize(image, N):
    ''' Function that gets an image, and a number N,
    limits the N shades to one shade according to the formula.'''
    new_image = []
    for row in range(len(image)):
        new_image.append([])
        for column in range(len(image[0])):
            new_image[row].append(round(math.floor((image[row][column]) * N
                                                   / 255) * 255 / N))
    return new_image


def quantize_colored_image(image, N):
    '''Function that gets a multicolored image and limits N shades,
    returns a quantized image'''
    separated_channels = separate_channels(image)
    new_image = []
    for channel in separated_channels:
        new_image.append(quantize(channel, N))
    return combine_channels(new_image)

def resize_3D(image, new_height, new_width):
    '''Function that resizes an image for multicolored
    images to new height and width'''
    separated_channels = separate_channels(image)
    new_image = []
    for channel in separated_channels:
        new_image.append(resize(channel, new_height, new_width))
    return combine_channels(new_image)


def add_mask(image1, image2, mask):
    '''Function that gets two images and a mask, combines the
    two images according to the mask and returns the new image'''
    new_image = []
    for row in range(len(image1)):
        new_image.append([])
        for column in range(len(image1[0])):
            if type(image1[row][column]) == list:
                lst = []
                for i in range(len(image1[row][column])):
                    lst.append(round(image1[row][column][i] *
                                     mask[row][column] +
                                     image2[row][column][i] *
                                     (1 - mask[row][column])))
                new_image[row].append(lst)
            else:
                new_image[row].append(round(image1[row][column] *
                                            mask[row][column] +
                                            image2[row][column] *
                                            (1 - mask[row][column])))
    return new_image


def image_to_mask(image):
    '''Function that gets an image and returns the mask of it'''
    mask = copy.deepcopy(image)
    for row in range(len(mask)):
        for column in range(len(mask[0])):
            mask[row][column] = mask[row][column] / 255
    return mask


def cartoonify(image, blur_size, th_block_size, th_c, quant_num_shades):
    """this function receives colored image, size of blur kernel,
    threshold block size, threshold constant and quantize shades number
    and returns a cartooned version of it"""

    quantized_image = quantize_colored_image(image, quant_num_shades)

    edges = get_edges(RGB2grayscale(image), blur_size, th_block_size,
                            th_c)
    edged_image_colored = combine_channels([edges, edges, edges])

    mask = image_to_mask(edges)

    cartooned_image = add_mask(quantized_image, edged_image_colored, mask)
    return cartooned_image


if __name__ == "__main__":

    if len(sys.argv) != 8:
        print("There's a problem")
        exit(1)

    image_source = sys.argv[1]
    cartoon_dest = sys.argv[2]
    max_size = int(sys.argv[3])
    blur_size = int(sys.argv[4])
    th_block_size = int(sys.argv[5])
    th_c = int(sys.argv[6])
    quant_num_shades = int(sys.argv[7])
    image = ex5_helper.load_image(image_source)

    new_height = len(image)
    new_width = len(image[0])

    if max_size < len(image):
        new_height = max_size
    if max_size < len(image[0]):
        new_width = max_size

    final_image = resize_3D(image, new_height, new_width)

    ex5_helper.save_image(cartoonify(final_image, blur_size, th_block_size,
                                     th_c, quant_num_shades), cartoon_dest)
