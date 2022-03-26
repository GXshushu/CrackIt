from encodings import utf_8
from threading import Thread
import zipfile
import os
import sys
import ctypes
def extractFile(zFile,password):
    global flag
    global passnum
    if flag == 1:
        return
    try:
        zFile.extractall(pwd=password.encode('ascii'))
        print("[+] 爆破成功密码为:" + password + "\n" + "尝试密码条数为:" + str(passnum+1))
        flag = 1
        return
    except Exception as result:
        # print("[-] 尝试失败:" + password + "\n")
        pass
    finally:
        passnum += 1

def crackIt(zFile,files):
    global passnum
    for passFile in files:
        with open("./dict/" + passFile) as wordlist:
            print("[+] 正在读取字典" + passFile)
            for line in wordlist.readlines():
                if flag == 1:
                    return
                password = line.strip('\n')
                t = Thread(target=extractFile,args=(zFile,password))
                t.start()
                t.join()

if __name__ == "__main__":
    flag = 0
    passnum = 0
    if len(sys.argv) != 2:
        print("[-] 命令格式有误,范例:python crackIt.py [ZipFilename]\n")
        sys.exit()
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print("[-] 文件"+filename+"不存在")
        sys.exit()
    if not os.access(filename,os.R_OK):
        print("[-] 文件"+filename+"拒绝访问")
        sys.exit()
    zFile = zipfile.ZipFile(filename)
    print("[+] 识别文件"+filename+"成功")
    try:
        files=os.listdir("./dict")
    except Exception as result:
        print("[-] 缺少dict目录\n")
        sys.exit()
    crackIt(zFile,files)
    
    if flag == 0:
        print("[-] 密码爆破失败！尝试密码条数为:" + str(passnum) + "\n")