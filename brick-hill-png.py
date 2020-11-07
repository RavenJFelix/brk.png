#!/usr/bin/env python


"""brick-hill-png.py: This glorious, absolutely amazinng and wonderful program converts"""
"""An image into a brk file."""

__author__ = "Raven Jyro \"G14989\" Felix"
__copyright__ = "MIT"

IMAGE_HEIGHT = 5

from PIL import Image 
import sys

MAX_8_BIT = 255

def percentize_tuple(le_tuple, max_value):
    percents = []
    for element in le_tuple:
        percents += [element / max_value]
    return tuple(percents)

def _test_percentize_tuple():
    """If the tuple is of 8 bit, then max_value is 255
        If a value is 255 it becomes 1."""
    test_tuple = (255, 221, 234)
    expected_tuple = (255/255, 221/255, 234/255)
    calculated_tuple = percentize_tuple(test_tuple, 255)
    assert calculated_tuple == expected_tuple

    test_tuple = (255, 221, 234, 0)
    expected_tuple = (255/255, 221/255, 234/255, 0/255)
    calculated_tuple = percentize_tuple(test_tuple, 255)
    assert calculated_tuple == expected_tuple

    test_tuple = (55, 21, 234, 0)
    expected_tuple = (255/255, 221/255, 234/255, 0/255)
    calculated_tuple = percentize_tuple(test_tuple, 255)
    assert not (calculated_tuple == expected_tuple)

def generate_brk_header():
    return (
    "B R I C K  W O R K S H O P  V0.2.0.0\n"
    "\n"
    "0 0 0\n"
    "0.14 0.51 0.20 1\n"
    "0.49 0.70 0.90\n"
    "100\n"
    "400")

def _test_generate_brk_header():
    1

def list_to_space_separated(array):
    output = ""
    for element in array:
        output += str(element) + " "
    return output[:-1] # Cut the superfluous space at the end

def _test_list_to_space_separated():
    test_array = [1, 2, 3, 4]
    expected = "1 2 3 4"
    output = list_to_space_separated(test_array)
    assert expected == output

def generate_brk_pixel_brick(position_tuple, color_rgba_8, name="Sharko"):
    position_string = list_to_space_separated(position_tuple)
    size_string = list_to_space_separated((1, 1, 1))
    color = percentize_tuple(color_rgba_8, MAX_8_BIT)
    color_string = list_to_space_separated(color)
    brick_header = position_string + " " + size_string + " " + color_string + '\n'
    brick_attributes = "\t+NAME " + name
    return brick_header + brick_attributes

def _test_generate_brk_pixel_brick():
    color_raw = (23, 43, 243)
    color = percentize_tuple(color_raw, MAX_8_BIT)
    color_string = list_to_space_separated(color)
    expected_value = ("1 2 3 1 1 1 " + color_string + "\n"
                     "\t+NAME Sharko")
    output = generate_brk_pixel_brick((1, 2, 3), color_raw)
    assert output == expected_value

def _test():
    _test_percentize_tuple()
    _test_generate_brk_header()
    _test_list_to_space_separated()
    _test_generate_brk_pixel_brick()

_test()

# file_name = "smolkek.png"
print(sys.argv[1])
file_name = sys.argv[1]
f = open(file_name + ".brk", "w+")
img = Image.open(file_name).convert(mode="RGBA")

f.write(generate_brk_header() + "\n")

for x in range(img.width):
    for y in range(img.height):
        color = img.getpixel((x, y))
        position = (x, y, IMAGE_HEIGHT)
        f.write(generate_brk_pixel_brick(position, color) + "\n")

f.close()
