import os, sys
from PIL import Image, ImageFilter

test = Image.open("./pixel.png")

rect = (50, 50, 200, 200)

region = test.crop(rect)

# region.show()

pixels = region.load() # create the pixel map

for i in range(region.size[0]):
    for j in range(region.size[1]):
        if pixels[i,j] != (255, 0, 0):
            pixels[i,j] = (255, 0 ,0)

test.paste(region, rect)
test.show()
