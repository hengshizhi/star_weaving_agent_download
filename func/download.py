import subprocess
import os
import base64
import json
import time
def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
        return True
    else:
        return False
def run(url,rootpath):
    '''
    url: baes64编码
    rootpath :根路径
    '''
    cmd = f'python ./operation/star_weaving_agent_download/func/download_shell.py --url {url} --path {rootpath}'
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
