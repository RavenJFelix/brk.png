#!/usr/bin/env python

"""brick-hill-png.py: This glorious, absolutely amazinng and wonderful program converts"""
"""An image into a brk file."""

__author__ = "Raven Jyro \"G14989\" Felix"
__copyright__ = "MIT"


from PIL import Image 
MAX_8_BIT = 255

def percentize_tuple(le_tuple, max_value):
    percents = []
    for element in le_tuple:
        percents += [element / max_value]
    return tuple(percents)

def _test_percentize_tuple():
    """If the tuple is of 8 bit, then max_value is 255
        If a value is 255 it becomes 1."""
    
    print("asdf")

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
    print(calculated_tuple)
    assert not (calculated_tuple == expected_tuple)

def generate_brk_header():
    return (
    "B R I C K  W O R K S H O P  V0.2.0.0\n"
    "\n"
    "0 0 0\n"
    "0.14 0.51 0.20 1\n"
    "0.49 0.70 0.90\n"
    "100\n"
    "400\n")

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

def generate_brk_pixel_brick(position_tuple, color_rgba, name="Sharko"):

def _test_generate_brk_pixel_brick():
    color_raw = (23, 43, 243)
    color = percentize_tuple(color_raw, MAX_8_BIT)
    expected_value = "1 2 3 1 1 1"


def _test():
    _test_percentize_tuple()
    _test_generate_brk_header()
    _test_list_to_space_separated()

_test()

print(generate_brk_header())
img = Image.open("roblox-logo.png").convert(mode="RGBA")
for x in range(img.width):
    for y in range(img.height):
        1
        #print("img.getpixel((x, y))")
