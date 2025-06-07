import webview
import os
import sys
import pathlib
import platform
from core import config
from core.log import logger
import asyncio

print(f"Python版本: {platform.python_version()}")

print(f"执行Python文件: {__file__}")
# 获取单文件缓存文件夹
# current_dir = os.path.dirname(os.path.abspath(__file__))
current_dir = os.path.dirname(__file__)
print(f"当前目录: {current_dir}")

print(f"当前程序二进制文件: {sys.executable}")

# 获取当前工作目录
current_work_dir = os.getcwd()
print(f"当前工作目录: {current_work_dir}")

# 拼接前端目录
web_dist_dir = pathlib.Path(current_dir).joinpath('dist').joinpath('index.html')
print(f"前端目录: {web_dist_dir}")

web_url = str(web_dist_dir)


config = asyncio.run(config.load_config())


if config.dev:
    logger.info("开发模式")
    web_url = 'http://localhost:5173'

def main(window):
    pass

window = webview.create_window('AG Launcher', web_url)


webview.start(main, args=[window], debug=True)

