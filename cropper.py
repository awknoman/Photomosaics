# This script if for cropping images into squares.
import os, sys
from PIL import Image

# Functions

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

# End of Functions List

# print(os.path.dirname(__file__))
directory = os.fsencode(os.path.dirname(__file__) + "\\images\\")
    
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    # print(filename)
    if filename.endswith(".jpg"):
        filePath = os.path.dirname(__file__) + "\\images\\" + filename
        croppedFilePath = os.path.dirname(__file__) + "\\cropped_images\\" + filename
        testImage = Image.open(filePath)
        # testImage.show()
        squareSize = min(testImage.width, testImage.height)
        crop = testImage.crop((0, 0, squareSize, squareSize))
        crop.save(croppedFilePath)
        # break
        avgColor = avg(testImage)
        print(avgColor)
    