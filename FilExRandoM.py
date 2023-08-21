#<\>!python3.11
#<\>coded by RMX
#----------------Don't Copy This Script--------------#
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('xdg-open https://facebook.com/groups/770617227293870/')
import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf ym.so')
except:
    pass
os.system('rm -rf ym.so')
os.system('git pull')

bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('ym.so'):
        os.system('curl -L https://github.com/YOUSUF-NIZAMI/FILExRANDOM/blob/main/ym.cpython-311.so?raw=true -o ym.so') 
        import ym
        #RMXXD.RM()
    else:
        import ym
        #RMXXD.RM()
elif bit == '32bit':
    exit('\033[1;31m\n Sorry System or 32bit device not supported ')
    
    

