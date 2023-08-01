# 1.代理下载
# 2.查看下载
# 1(1):通过ip地址指定，限制ip地址的使用量
from .func.download import mkdir
import operation.star_weaving_agent_download.func as func
from sanic.response import text
mkdir('./cache_download_files/')

def new_download_api(get_or_post, enableSession, rep, **para):
    return rep(text(func.new_download(get_or_post('url'),para['request'].ip)))

def download_api(get_or_post, enableSession, rep, **para):
    return rep(func.download(get_or_post('url')))

def download_file_api(get_or_post, enableSession, rep, **para):
    return rep(func.download_file(get_or_post('url')),_async=True)
def top_execution_queue_api(get_or_post, enableSession, rep, **para):
    if (get_or_post('secret-key') == '114514'):
        func.top_execution_queue()
    return rep('OK')

api = {
    'new-download':new_download_api,
    'download':download_api,
    'download-file':download_file_api,
    'top_execution_queue':top_execution_queue_api
}