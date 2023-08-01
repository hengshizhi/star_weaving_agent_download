from .download import run as download_run
from .download import mkdir
from operation.md5 import get_md5 as md5
from os.path import normpath
def download(url,ip):
    path = normpath(f'./cache_download_files/{md5(url)}')
    mkdir(path)
    download_run(url,path)
