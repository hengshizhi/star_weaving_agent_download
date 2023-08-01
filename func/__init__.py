from .download import run as download_run
from .download import mkdir
from operation.md5 import get_md5 as md5
from os.path import normpath
from sanic.response import file_stream,text
import os
import json
def new_download(url,ip):
    path = normpath(f'./cache_download_files/{md5(url)}')
    mkdir(path)
    download_run(url,path)

def download_file(url):
    root_path =  f'./cache_download_files/{url}/'
    list_f = os.listdir(root_path)
    return file_stream(f'{root_path}{list_f[0]}')

def download(url):
    url = md5(url)
    root_path =  f'./cache_download_files/{url}/'
    list_f = os.listdir(root_path)
    return text(json.dumps({
        'url':f'/api/download-file?url={url}',
        'file_name':list_f[0]
    }))