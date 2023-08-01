import subprocess
import os
import base64
def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
        return True
    else:
        return False
def run(url,rootpath):
    cmd = f'python .\operation\star_weaving_agent_download\\func\download_shell.py --url {url} --path {rootpath}'
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
# if __name__ == '__main__':
#     p = run('http://dl_dir.qq.com/qqfile/qq/QQ2011/QQ2011.exe','./QQ/')
