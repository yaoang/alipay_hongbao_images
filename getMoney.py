#!/usr/bin/env python
# created by yao
# 2016.12.23
from PIL import Image
im = Image.open('1239788822.jpg')

imgWidth = 370 # width of the image you cut off
startY = 10 # the first line position-y
splitPoxis = 13 # split height
blackHeigh = 6 # black line height
maxLineNumber = 27


# function to deal image
def pasteImg( startY, index):
    box = (1, startY + splitPoxis*index-blackHeigh,imgWidth,startY + splitPoxis*index)
    region = im.crop(box)
    
    box_dealed = (1,startY + splitPoxis * index,imgWidth,startY + splitPoxis*index+blackHeigh)
    region_dealed = im.crop(box_dealed)
    
    im.paste( region, box_dealed )


pasteImg(startY, 0)

for index in range(1,maxLineNumber):
    pasteImg( startY, index )


im.save('1239788822.dealed.jpg')
im.show()