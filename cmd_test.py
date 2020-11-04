import pyautogui as pgui
import time
import pyperclip

def ckytj_start(x):
    pgui.PAUSE = x
    pgui.FAILSAFE = True           # 启用自动防故障功能
    width,height = pgui.size()     # 屏幕的宽度和高度
    pgui.position()                # 鼠标当前位置

def pause_start(x):##时间设置
    pgui.PAUSE = x
    
def paste(foo):
    pyperclip.copy(foo)
    pgui.hotkey('ctrl', 'v')
    
def win_test(): ### i为全能串口window位置
    pause_start(0.5)
    pgui.keyDown ('altleft')
    pgui.press ('tab')
    pgui.keyUp ('altleft')
ck = u'/c'
def call_cmd(foo=u'start dir'):
    
    pgui.keyDown ('winleft')
    pgui.press ('r')
    pgui.keyUp ('winleft')
    cmd_foo=u'cmd'+' '+ck+' '+foo
    paste(cmd_foo)
    pgui.press ('enter')
def attrib_r(attrib_puth='C:\\Windows\\yktcfg.ini'):
    global ck
    ck = u'/c'
    call_cmd('attrib -r '+attrib_puth)
    
def copyini(copy_puth):
    global ck
    ck = u'/c'
    copy_puth1='copy /Y '
    copy_puth2='  C:\\Windows\\yktcfg.ini'
    call_cmd(copy_puth1+copy_puth+copy_puth2)
    
    
def delini():
    global ck
    ck = u'/c'
    call_cmd('del /F C:\\Windows\\yktcfg.ini')
if __name__ == '__main__':
    ckytj_start(0.15)
    ck =u'/c'
    call_cmd(u'copy /Y H:\\15寸屏参\\15寸\\rockadb  H:\\')
