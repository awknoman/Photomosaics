import os, sys
from PIL import Image

# Creating a pixelated image of given image

# FUNCTIONS LIST.

# For calculating average pixel color of a section of image
def avg(section):

    # Understanding why below statement is required.
    sec = section.convert("RGB")

    # Initializing values
    r = g = b = 0

    width = sec.width
    height = sec.height

    # Couldn't think of any other variable name
    divideBy = width * height

    for i in range(0, width):
        for j in range(0, height):
            r += sec.getpixel((i, j))[0] / divideBy
            g += sec.getpixel((i, j))[1] / divideBy
            b += sec.getpixel((i, j))[2] / divideBy

    meanTuple = (int(r), int(g), int(b))
    return meanTuple

def applyColor(region, color):
    pixels = region.load()
    for i in range(0, region.width):
        for j in range(0, region.height):
            pixels[i, j] = color

    return region

# END OF FUNCTIONS LIST.

# Loading an Image to Image object.
testImage = Image.open("./pixel.png")

# Specifying the square view for calculating average color
square = (10, 10)

# Creating a blank Image object.
newImage = Image.new("RGB", (testImage.width, testImage.height))

for i in range(0, testImage.width, square[0]):
    for j in range(0, testImage.height, square[1]):
        region = testImage.crop((i, j, i + square[0], j + square[1]))
        avgColor = avg(region)
        region = applyColor(region, avgColor)
        newImage.paste(region, (i, j, i + square[0], j + square[1]))

newImage.show()
