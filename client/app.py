import webview
import os, pathlib

print(f"执行Python文件: {__file__}")
# 获取单文件缓存文件夹
current_dir = os.path.dirname(os.path.abspath(__file__))
print(f"当前目录: {current_dir}")
# print(sys.executable)

# 获取当前工作目录
current_work_dir = os.getcwd()
print(f"当前工作目录: {current_work_dir}")

# 拼接前端目录
web_dist_dir = pathlib.Path(current_dir).joinpath('dist').joinpath('index.html')
print(f"前端目录: {web_dist_dir}")

window = webview.create_window('AG Launcher', str(web_dist_dir))
webview.start(debug=True)

