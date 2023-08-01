from .download import run as download_run
from .download import mkdir
from operation.md5 import get_md5 as md5
from os.path import normpath
from sanic.response import file_stream,text
import os
import json
import time
def kill_aria2c():
    '''杀死所有aria2c进程'''
    os.system('pkill aria2c')

def get_file_access_time(filePath):
    '''获取文件的访问时间'''
    t = os.path.getatime(filePath)
    return t

def CAPACITY():
    '''
    获取磁盘使用率
    '''
    info = os.statvfs('/')
    free_size = info.f_bsize * info.f_bavail / 1024 / 1024
    total_size = info.f_blocks * info.f_bsize / 1024 / 1024
    return free_size / total_size * 100

def get_queue():
    try:
        with open('./swad_data/queue.json','r') as fr:
            data = json.loads(fr.read())
            return data
    except:
        with open('./swad_data/queue.json','w') as f:f.write(json.dumps([]))
        return None

def add_queue(url,ip):
    try:
        with open('./swad_data/queue.json','r') as fr:
            data = json.loads(fr.read())
            data.append({'url':url,'ip':ip,'time':time.time()})
            with open('./swad_data/queue.json','w') as fw:fw.write(json.dumps(data))
            return data
    except:
        with open('./swad_data/queue.json','w') as f:f.write(json.dumps([{'url':url,'ip':ip,'time':time.time()}]))
        return None

def renew_accessed(url):
    try:
        with open('./swad_data/Accessed.json','r') as fr:
            data = json.loads(fr.read())
            data[url] = time.time()
            with open('./swad_data/Accessed.json','w') as fw:fw.write(json.dumps(data))
            return data
    except:
        with open('./swad_data/Accessed.json','w') as f:f.write(json.dumps({url:time.time()}))
        return None

def queue_index(queue:list,url):
    index = 0
    for i in queue:
        index += 1
        if (i['url'] == url):
            return index
    return False
def new_download(url,ip):
    path = normpath(f'./cache_download_files/{md5(url)}')
    if (md5(url) in os.listdir('./cache_download_files/')):
        return f'Download completed, URL: /api/download?url={url}'
    queue_list = get_queue()
    index = queue_index(queue_list, url)
    if (not index or queue_list == []):
        queue_list = add_queue(url,ip)
        index = 1
    if (index == 1):
        mkdir(path)
        download_run(url,path)
        return 'Start downloading'
    else:
        return f'Queuing, you are in position {index}'

def download_file(url):
    root_path =  f'./cache_download_files/{url}/'
    list_f = os.listdir(root_path)
    return file_stream(f'{root_path}{list_f[0]}')

def download(url):
    renew_accessed(url)
    url = md5(url)
    root_path =  f'./cache_download_files/{url}/'
    list_f = os.listdir(root_path)
    return text(json.dumps({
        'url':f'/api/download-file?url={url}',
        'file_name':list_f[0]
    }))

def top_execution_queue():
    # kill_aria2c() # 执行之前杀死所有aria2c进程
    queue = get_queue()
    if (queue == []):
        pass
    else:
        queue = queue[0]
        url = queue['url']
        path = normpath(f'./cache_download_files/{md5(url)}')
        download_run(url,path)