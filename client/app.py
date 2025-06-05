import webview
import os
import sys
import pathlib
import platform
from core import config

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

# debug = True
debug = False

if debug:
    web_url = 'http://localhost:5173'

def main(window):
    # window.evaluate_js("alert('Hello World!')")
    window.run_js("alert('Hello World!')")

window = webview.create_window('AG Launcher', web_url)


webview.start(main, args=[window], debug=True)

