import sys
import os
print(sys.argv[1])
name='day'+sys.argv[1]+'_朱时韵.tar.gz '  #拼名字
print(name)
#os.system是Python调用bash shell的函数
os.system('tar czf '+name+"*.py")  #压缩
str_scp='scp '+name+' python8@42.192.117.114:~/day'+sys.argv[1]
os.system(str_scp)