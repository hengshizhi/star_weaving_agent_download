# 1.代理下载
# 2.查看下载
# 1(1):通过ip地址指定，限制ip地址的使用量
from .func.download import mkdir
import operation.star_weaving_agent_download.func as func
from sanic.response import text
mkdir('./cache_download_files/')

def new_download_api(get_or_post, enableSession, rep, **para):
    func.new_download(get_or_post('url'),para['request'].ip)
    return rep(text('OK'))

def download_api(get_or_post, enableSession, rep, **para):
    return rep(func.download(get_or_post('url')))

def download_file_api(get_or_post, enableSession, rep, **para):
    return rep(func.download_file(get_or_post('url')),_async=True)

api = {
    'new-download':new_download_api,
    'download':download_api,
    'download-file':download_file_api
}