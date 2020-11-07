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


def _test():
    _test_percentize_tuple()

_test()

print("Frick")
img = Image.open("roblox-logo.png").convert(mode="RGBA")
print(img.width)
for x in range(img.width):
    for y in range(img.height):
        #print("img.getpixel((x, y))")
