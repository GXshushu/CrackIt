# CrackIt
一个轻型的字典爆破zip压缩文件解压密码的python脚本
目前已支持rar以及7z压缩文件爆破，需要安装rar的依赖http://www.rarlab.com/rar/UnRARDLL.exe。
参考安装unrar模块以及相关依赖教程，https://blog.csdn.net/big_talent/article/details/52367184
7z压缩包爆破能力较弱，希望大佬们多提宝贵意见。

如果不想使用爆破rar功能可以不安装相关依赖，把第七行和第77到第79行注释掉就可以运行了。
```python
7   # from unrar import rarfile

77  # elif filename.endswith(".rar"):
78  #     rFile = rarfile.RarFile(filename)
79  #     crackIt(rFile,files,"rar")
```
## 字典更换
只要把字典文件放进./dict里面，运行的时候就会自动读取
## 运行
python crackIt.py [ZipFilename|RarFilename|7zFilename]
## 测试
python crackIt.py testZip_2.zip
