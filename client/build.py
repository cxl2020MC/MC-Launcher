import os
import shutil
import subprocess
import platform


print('当前操作系统：', platform.system())

print(f'当前工作目录：{os.getcwd()}')

print('切换工作目录到web')

os.chdir('../web')
print(f'当前工作目录：{os.getcwd()}')

print('开始构建前端')

subprocess.run("pnpm build", shell=True)

print('切换工作目录到client')

os.chdir('../client')
print(f'当前工作目录：{os.getcwd()}')


print('开始构建客户端')


bulid_commend = "nuitka --onefile app.py --include-data-dir=../web/dist=dist --output-dir=nuitka_dist --remove-output --assume-yes-for-downloads"
if platform.system() == 'Darwin':
    bulid_commend += "--macos-create-app-bundle"
subprocess.run(bulid_commend, shell=True)
# subprocess.run(['nuitka', '--mode=standalone', 'app.py', '--include-data-dir=../web/dist=dist'], shell=True)


print('构建完成')