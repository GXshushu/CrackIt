from encodings import utf_8
from threading import Thread
from multiprocessing import  Process
import zipfile
import os
import sys
from unrar import rarfile
import py7zr

Glo_password = ""

def extractFile(File,password,type):
    global flag
    global passnum
    global Glo_password
    if flag == 1:
        return
    try:
        if type == "zip":
            File.extractall(pwd=password.encode('ascii'))
            print("[+] 爆破成功密码为:" + password + "\n" + "[*] 尝试密码条数为:" + str(passnum+1))
            flag = 1
            Glo_password = password
            return
        elif type == "rar":
            File.extractall("./output",pwd=password)
            print("[+] 爆破成功密码为:" + password + "\n" + "[*] 尝试密码条数为:" + str(passnum+1))
            flag = 1
            Glo_password = password
            return
        elif type == "7z":
            py7zr.SevenZipFile(File, mode='r', password=password).extractall()
            print("[+] 爆破成功密码为:" + password + "\n" + "[*] 尝试密码条数为:" + str(passnum+1))
            flag = 1
            Glo_password = password
            return
    except Exception as e:
        # print("[-] 尝试失败:" + password + "\n")
        pass
    finally:
        passnum += 1

def crackIt(File,files,type):
    global passnum
    for passFile in files:
        with open("./dict/" + passFile) as wordlist:
            print("[+] 正在读取字典" + passFile)
            for line in wordlist.readlines():
                if flag == 1:
                    return
                password = line.strip('\n')
                t = Thread(target=extractFile,args=(File,password,type))
                t.start()

if __name__ == "__main__":
    flag = 0
    passnum = 0
    if len(sys.argv) != 2:
        print("[-] 命令格式有误,范例:python crackIt.py [ZipFilename]\n")
        sys.exit()
    filename = sys.argv[1]
    try:
        files=os.listdir("./dict")
    except Exception as result:
        print("[-] 缺少dict目录\n")
        sys.exit()
    if not os.path.isfile(filename):
        print("[-] 文件"+filename+"不存在")
        sys.exit()
    if not os.access(filename,os.R_OK):
        print("[-] 文件"+filename+"拒绝访问")
        sys.exit()
    if filename.endswith(".zip"):
        zFile = zipfile.ZipFile(filename)
        print("[+] 识别zip文件"+filename+"成功")
        crackIt(zFile,files,"zip")
    elif filename.endswith(".rar"):
        rFile = rarfile.RarFile(filename)
        crackIt(rFile,files,"rar")
    elif filename.endswith(".7z"):
        crackIt(filename,files,"7z")
    if flag == 0:
        print("[-] 密码爆破失败！尝试密码条数为:" + str(passnum) + "\n")
    else:
        print("--------------------------------------------------------\n[+] 密码:"+Glo_password)
    