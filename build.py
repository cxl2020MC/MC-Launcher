import os
import shutil
import subprocess

print(f'当前工作目录：{os.getcwd()}')

print('切换工作目录到web')

os.chdir('web')
print(f'当前工作目录：{os.getcwd()}')

print('开始构建前端')

subprocess.run(['pnpm', 'build'], shell=True)

print('切换工作目录到client')

os.chdir('../client')
print(f'当前工作目录：{os.getcwd()}')

print('删除旧的前端文件')

shutil.rmtree('dist', ignore_errors=True)

# print('复制前端文件到客户端')

# shutil.copytree('../web/dist', 'dist', dirs_exist_ok=True)

# print('复制完成')

print('开始构建客户端')

subprocess.run(['nuitka', '--onefile', 'app.py', '--include-data-dir=../web/dist=dist'], shell=True)
# subprocess.run(['nuitka', '--mode=standalone', 'app.py', '--include-data-dir=../web/dist=dist'], shell=True)


print('构建完成')
# print('删除前端文件')

# shutil.rmtree('dist', ignore_errors=True)