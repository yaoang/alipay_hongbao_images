# alipay_hongbao_images
支付包AR红包黑线去除算法

直接修改getMoney.py
自己根据图片不同情况，去修改参数：  
`imgWidth = 370` # width of the image you cut off  
`startY = 10` # the first line position-y  
`splitPoxis = 13` # split height  
`blackHeigh = 6` # black line height  
`maxLineNumber = 27`  #numbers of the black lines

第二个程序getMoney_iphone_6sp.py 更实用  
直接全屏抓图，也是修改参数就行。(其实与第一个没有本质差别)  
