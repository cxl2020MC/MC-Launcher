import sys
import platform
import asyncio
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from core.log import logger
from core import config

# nuitka-project: --onefile
# nuitka-project: --include-data-dir=../web/dist=dist
# nuitka-project: --output-dir=nuitka_dist
# nuitka-project: --remove-output
# nuitka-project: --assume-yes-for-downloads
# nuitka-project-if: {OS} in ("Darwin"):
#    nuitka-project: --macos-create-app-bundle

logger.debug(f"Python版本: {platform.python_version()}")

logger.debug(f"执行Python文件: {__file__}")

# 获取单文件缓存文件夹
current_dir = Path(__file__).parent  # .resolve()
logger.debug(f"当前目录: {current_dir}")

logger.debug(f"当前程序二进制文件: {sys.executable}")

# 获取当前工作目录
current_work_dir = Path.cwd()
logger.debug(f"当前工作目录: {current_work_dir}")

# 拼接前端目录
web_dist_dir = current_dir / 'dist/index.html'
logger.debug(f"前端目录: {web_dist_dir}")

config_data = asyncio.run(config.load_config())


if config_data.dev:
    logger.info("开发模式已启用!")

app = FastAPI()
app.mount('/', StaticFiles(directory=web_dist_dir.parent, html=True))

if __name__ == '__main__':
    import webbrowser
    import uvicorn
    webbrowser.open_new_tab("http://localhost:8000/index.html")
    uvicorn.run(app, host="0.0.0.0", port=8000)
