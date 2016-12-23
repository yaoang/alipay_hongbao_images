#!/usr/bin/env python
# created by yao
# 2016.12.23
from PIL import Image
im = Image.open('263229550.jpg')

imgWidth = 370 # width of the image you cut off
startX = 221
startY = 699 # the first line position-y
splitPoxis = 13 # split height
blackHeigh = 6 # black line height
maxLineNumber = 27


# function to deal image
def pasteImg( startY, index):
    box = (startX, startY + splitPoxis*index-blackHeigh,startX + imgWidth,startY + splitPoxis*index)
    #print box
    region = im.crop(box)
    
    box_dealed = (startX,startY + splitPoxis * index,startX + imgWidth,startY + splitPoxis*index+blackHeigh)
    #print box
    region_dealed = im.crop(box_dealed)
    
    im.paste( region, box_dealed )


pasteImg(startY, 0)

for index in range(1,maxLineNumber):
    pasteImg( startY, index )


im.save('263229550.dealed.jpg')
im.show()