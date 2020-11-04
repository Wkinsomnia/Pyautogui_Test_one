import os
import os.path
import sys
import configparser
sys.path.append(r'D:\ProgramFiles\Python\workspeces')
import cmd_test as c
import pypinyin as piy
# This folder is custom

def os_listdir(path = ('E:\\xieyi')):

    
    f = os.listdir(path) #将文件名提取为一个列表当中
    for i in f:
        print(i)
    k = 0
    n = 0
    for i in f:
        if '副本' in i:
            oldname = i  
            matchObj = oldname.split(' - ') #如果是面对复杂一点的结构，可以用正则表达式re.match('(A\d+\-)(.*\-1\-)(.*)',string),然后取其group(1)和group(3)
            newname = (''.join(piy.lazy_pinyin(matchObj[0])))
            os.renames(path+'\\'+oldname,path+'\\'+newname)
            k+=1
        else:
            pass
        n+=1
    print('已经修改了%d个文件名'% k)

def paret(scanf='克'):
    rootdir ='E:\\xieyi'
    '''
    for dirname in dirnames:
        print(" ", parent)
    '''
    parent_sz=['0']
    for parent, dirnames, filenames in os.walk(rootdir):
    # Case1: traversal the directories
        for filenames in filenames:
            parent_sz.append(parent.replace('/','\\'))
            #print(" ", parent.replace('/','\\')+'\\'+filenames)
            configPath=parent.replace('/','\\')+'\\'+filenames
        
            if (''.join(piy.lazy_pinyin(scanf))) in configPath:
                print(" ", parent.replace('/','\\')+'\\'+filenames)
                return configPath
            
''' 
    # Case2: traversal the files
        for filenames in filenames:
            print("Parent folder:", parent)
            print("Filename:", filenames)
    
'''

def config_read(configPath):
    global comfig
    print(config.sections())        #  []
    config.read(configPath)
    print(config.sections())        #   ['bitbucket.org', 'topsecret.server.com']
    print('Protocol' in config) # False
    print('Command' in config) # True
    '''
    yktcfg_Protocol=config.items('Protocol')
    yktcfg_Command=config.items('Command')
    for yktcfg in config.items('Protocol'):
        print(('Protocol',)+yktcfg[:])
    for yktcfg in config.items('Command'):
        print(('Command',)+yktcfg[:])
    '''
    print('['+'Protocol'+']')
    for yktcfg in config.items('Protocol'):
        
        print(('='.join(yktcfg[:])).title())
    print('['+'Command'+']')
    for yktcfg in config.items('Command'):
        print(('='.join(yktcfg[:])).title())
def read_print(configPath):
    global comfig
    config = configparser.ConfigParser()
    config.read(configPath,encoding='utf-8')
    dic = dict(config._sections)
    for i in dic:
        dic[i] = dict(dic[i])
    print(dic)
def config_write(configPath='C:/Windows/yktcfg.ini'):
    global comfig
    c.attrib_r()
    config.write(open(configPath.replace('/','\\'), "w"))
def config_remove():
    global comfig
    config.remove_section('Protocol')
    config.remove_section('Command')
    config.clear()
    config.write(open(configPath.replace('/','\\'), "w"))
config = configparser.ConfigParser()
def main():
    c.ckytj_start(0.15)
    while True:
        try :
            scanf=input('del/copy//write/remove:\n')
            
            if 'd' in scanf :
                c.delini()
            elif 'c' in scanf :
                copy_name = input('协议名:\n')
                c.copyini(paret(copy_name))
            elif 'w' :
                copy_name = input('协议名:\n')
                
                config_write(paret(copy_name))
            elif 'r' :
                config_remove()
            else :
                continue
        except :
            print("请重新输入")
            continue

  
if __name__ == '__main__':
    
    ##print(paret(''))
    paret_name = input('协议名')
    if paret_name.isspace():
        paret_name = '德有'
    config_read(paret(paret_name))
    main()
    ##config_write()
    

