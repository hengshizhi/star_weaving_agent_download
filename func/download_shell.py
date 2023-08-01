# 使用方法： 
# 参数 : --url , --path

def arg(_,__): #接收命令行参数
    import sys
    import getopt
    '''参数:
    _ :短参数str,列如：-f-g-p
    __:长参数list,列如：['file','get','post']
    返回示例:{'-g': 'aa', '-f': 'aaa', '-p': 'huagsu.py'}
    '''
    arg = getopt.getopt(sys.argv[1:],_,__)
    arg[1].insert(0,arg[0][0][0])
    ditcr = {}
    for i in range(len(arg[1])):
        if((i+1) % 2 == 0):
            ditcr[arg[1][i-1]] = arg[1][i]
    return ditcr
def mkdir(path):
    import os
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
        return True
    else:
        return False

import subprocess
import os
import base64
from urllib.parse import quote
import json
import time
import requests
port = 7000
def b64decode(s):
    return str(base64.b64decode(s), "utf-8")
arg_data = arg('',['url','path'])
root_path = arg_data['--path']
url = b64decode(arg_data['--url'])
if ('https:' in url):
    url = 'https:'+quote(url.replace('https:',''),encoding = 'utf-8')
else:
    url = 'http:'+quote(url.replace('http:',''),encoding = 'utf-8')
mkdir(root_path)
os.chdir(root_path) # 更改运行路径
cmd= f'aria2c --console-log-level=error -c -x 16 -s 16 {url}'
complete = subprocess.call(cmd, shell=True)

with open('../../swad_data/queue.json','r') as fr: # 更改队列
    data = json.loads(fr.read())
    del data[0]
    with open('../../swad_data/queue.json','w') as fw:fw.write(json.dumps(data))

secret_key = '114514'
requests.get(f'https://dsw-gateway-cn-hangzhou.data.aliyun.com/dsw-75218/ide/proxy/7000/api/top_execution_queue?secret-key={secret_key}&xv=1') # 继续执行队列