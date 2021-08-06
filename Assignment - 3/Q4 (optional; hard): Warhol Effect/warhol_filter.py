"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg'

def main():
    blank_image = SimpleImage.blank(WIDTH, HEIGHT)

    # TODO: your code here
    pink_patch = make_recolored_patch(1.5, 0, 1.5)  # This is an example which should generate a pinkish patch
    a_patch = make_recolored_patch(1, 1, 1)  # Original image
    b_patch = make_recolored_patch(0, 1.5, 0)  # This is an example which should generate a green patch
    c_patch = make_recolored_patch(1.9, 1.9, 1.9)  # This is an example which should generate a brighter patch
    d_patch = make_recolored_patch(0.1, 0.3, 2)  # This is an example which should generate a blue patch
    e_patch = make_recolored_patch(1.5, 1.7, 0.5)  # This is an example which should generate a yellow patch


    warhol_image(blank_image, pink_patch, 0, 0)
    warhol_image(blank_image, a_patch, 1, 0)
    warhol_image(blank_image, b_patch, 2, 0)
    warhol_image(blank_image, c_patch, 0, 1)
    warhol_image(blank_image, d_patch, 1, 1)
    final_image = warhol_image(blank_image, e_patch, 2, 1)

    final_image.show()


def make_recolored_patch(red_scale, green_scale, blue_scale):
    '''
    Implement this function to make a patch for the Warhol Filter.
    It loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixel's red component by
    :param green_scale: A number to multiply each pixel's green component by
    :param blue_scale: A number to multiply each pixel's blue component by
    Returns the newly generated patch.
    '''
    patch = SimpleImage(PATCH_NAME)
    # TODO: your code here
    for y in range(patch.height):
        for x in range(patch.width):
            pixel = patch.get_pixel(x, y)
            pixel.red = pixel.red * red_scale
            pixel.green = pixel.green * green_scale
            pixel.blue = pixel.blue * blue_scale
    return patch


def warhol_image(image, patch, x_image_order, y_image_order):
    """
    Places one patched image inside a blank image in the given X and Y coordinates
    :param image: a blank image that a size that fits 6 patched images (in 2 rows and 3 columns)
    :param patch: patched image
    :param x_image_order: order of the image in X coordinate
    :param y_image_order: order of the image in Y coordinate
    :return: An image with one patched image placed at a given X and Y coordinates
    """
    width = patch.width
    height = patch.height
    for y in range(patch.height):
        for x in range(patch.width):
            start_x = x + width * x_image_order  # X coordinate for image to be placed
            start_y = y + height * y_image_order  # Y coordinate for image to be placed
            pixel = patch.get_pixel(x, y)
            image.set_pixel(start_x, start_y, pixel)
    return image


if __name__ == '__main__':
    main()

   
