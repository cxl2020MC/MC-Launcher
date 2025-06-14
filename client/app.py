import webview
import os
import sys
import pathlib
import platform
import asyncio

from core.log import logger
from core import config
from core.js_api import Api


logger.debug(f"Python版本: {platform.python_version()}")

logger.debug(f"执行Python文件: {__file__}")
# 获取单文件缓存文件夹
# current_dir = os.path.dirname(os.path.abspath(__file__))
current_dir = os.path.dirname(__file__)
logger.debug(f"当前目录: {current_dir}")

logger.debug(f"当前程序二进制文件: {sys.executable}")

# 获取当前工作目录
current_work_dir = os.getcwd()
logger.debug(f"当前工作目录: {current_work_dir}")

# 拼接前端目录
web_dist_dir = pathlib.Path(current_dir).joinpath('dist').joinpath('index.html')
logger.debug(f"前端目录: {web_dist_dir}")

web_url = str(web_dist_dir)

config_data = asyncio.run(config.load_config())


if config_data.dev:
    logger.info("开发模式已启用!")
    web_url = 'http://localhost:5173'
    logger.info(f"设置URL为 {web_url}")

def main(window: webview.Window, config_data: config.Config):
    pass


if __name__ == '__main__':
    js_api = Api()
    js_api.start_loop()
    window = webview.create_window('AG Launcher', web_url, js_api=js_api)

    webview.start(main, args=[window, config_data], debug=config_data.debug)
