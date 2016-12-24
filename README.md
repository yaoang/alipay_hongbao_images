# 支付包AR红包黑线去除小程序
支付包AR红包黑线去除小程序
--------------
Author: yaoang  
weixin: fyan888  

尽量使用iphone_6sp那个，第一个程序已经停止维护。  
目前主要针对iphone6sp进行升级。  
支付宝第二次修改，今天下午已经解决，并且扫了十个。  

直接修改getMoney.py
自己根据图片不同情况，去修改参数：  
`imgWidth = 370` # width of the image you cut off  
`startY = 10` # the first line position-y  
`splitPoxis = 13` # split height  
`blackHeigh = 6` # black line height  
`maxLineNumber = 27`  #numbers of the black lines

第二个程序getMoney_iphone_6sp.py 更实用  
直接全屏抓图，也是修改参数就行。(其实与第一个没有本质差别)  
