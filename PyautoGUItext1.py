import pyautogui
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True           # 启用自动防故障功能
width,height = pyautogui.size()     # 屏幕的宽度和高度
pyautogui.position()                # 鼠标当前位置
 
## 控制鼠标移动
'''
# 获取鼠标当前位置
x,y = pyautogui.position()
        positionStr = 'X: '+str(x).rjust(4)+' Y:'+str(y).rjust(4)
'''
print('Press Ctrl-C to quit.')
try:
    while True:
        # Get and print the mouse coordinates.
        x,y = pyautogui.position()
        positionStr = 'X: '+str(x).rjust(4)+' Y:'+str(y).rjust(4)
        pix = pyautogui.screenshot().getpixel((x,y))   # 获取鼠标所在屏幕点的RGB颜色
        positionStr += 'RGB:('+str(pix[0]).rjust(3)+','+str(pix[1]).rjust(3)+','+str(pix[2]).rjust(3)+')'
        print(positionStr,end='')                      # end='' 替换了默认的换行
        print('\b'*len(positionStr),end='',flush=True) # 连续退格键并刷新，删除之前打印的坐标，就像直接更新坐标效果
        print('\n')
except KeyboardInterrupt:                              # 处理 Ctrl-C 按键
    print('\nDone.')
