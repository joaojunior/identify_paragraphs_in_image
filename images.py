from itertools import groupby
from operator import itemgetter

import numpy as np
from PIL import Image, ImageDraw, ImageFont
import cv2


def text_to_image(text, file_name, background=(255, 255, 255),
                  font_color=(0, 0, 0), font=ImageFont.load_default(),
                  size=(500, 250)):
    """
    This function receive a text and create a image file with this
    text. The parameter `text` is the text to generate a image,
    `file_name` is the name of file to save the image, `background`
    is the color in format RGB to background of the image. The
    default value to this parameter is the color white(255, 255, 255).
    The `font_color` is the color, in RGB, of the text. The default
    value of this parameter is black(0, 0, 0). The parameter `font`
    is the font to generate the image and the default value is the
    font of the system. The last parameter `size` is the size of the
    image generated.
    """
    image = Image.new("RGB", size, background)
    draw = ImageDraw.Draw(image)
    y_text = 0
    for line in text.split("\n"):
        width, height = font.getsize(line)
        draw.text((0, y_text), line, font=font, fill=font_color)
        y_text += height
    image.save(file_name)
    return image


def remove_boundary(image, background_color=255):
    """
    This function remove lines on the top and the bottom and
    columns in the right and the left with the color equal
    the parameter `background`. The function looking for lines and
    columns with the color `background` and remove these before
    found any another color.
    The parameter `image` is an image of opencv
    """
    index_top_rows = 0
    index_bottom_rows = -1
    index_left_columns = 0
    index_right_columns = -1
    rows_axis = 0
    columns_axis = 1
    operations = [(index_left_columns, columns_axis),
                  (index_right_columns, columns_axis),
                  (index_top_rows, rows_axis),
                  (index_bottom_rows, rows_axis)]
    for index, axis in operations:
        size = image.shape[1 - axis]
        removed = True
        while removed:
            data = image.take(axis=axis, indices=[index])
            average = data.sum() / size
            if average == background_color:
                image = np.delete(image, index, axis)
            else:
                removed = False
    return image


def get_lines_with_color(image, color=255):
    y_size, x_size = image.shape
    lines = []
    for row in range(y_size):
        data = image.take(axis=0, indices=[row])
        average = data.sum() / x_size
        if average == color:
            lines.append(row)
    return lines


def identify_paragraphs_in_image(image):
    image = remove_boundary(image)
    blank_lines = get_lines_with_color(image)
    y_size, x_size = image.shape
    min_space = y_size
    max_space = 0
    idx_min_max_blank_lines = []
    sizes = []
    for k, g in groupby(enumerate(blank_lines), lambda x: x[1]-x[0]):
        line = list(map(itemgetter(1), g))
        size = line[-1] - line[0] + 1
        sizes.append(size)
        idx_min_max_blank_lines.append((line[0], line[-1]))
        if(size < min_space):
            min_space = size
        if(size > max_space):
            max_space = size
    number_paragraphs = 0
    for idx_min, idx_max in idx_min_max_blank_lines:
        if (idx_max - idx_min + 1 >= np.percentile(list(set(sizes)), 50)):
            line = int((idx_min+idx_max) / 2)
            cv2.line(image, (0, line), (x_size, line), (0, 0, 0))
            number_paragraphs += 1
    return number_paragraphs+1, image
