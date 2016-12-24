#!/usr/bin/env python
# created by yao
# 2016.12.23
from PIL import Image
im = Image.open('IMG_0170.PNG')

imgWidth = 570 # width of the image you cut off
startX = 307
startY = 972 # the first line position-y
splitPoxis = 18 # split height
blackHeigh = 8 # black line height
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


im.save('IMG_0170.dealed.jpg')
im.show()