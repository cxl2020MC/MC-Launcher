import os
import shutil
import subprocess
import platform


shell = True
print('当前操作系统：', platform.system())
if platform.system() != 'Windows':
    print("关闭shell=True")
    shell = False



print(f'当前工作目录：{os.getcwd()}')

print('切换工作目录到web')

os.chdir('../web')
print(f'当前工作目录：{os.getcwd()}')

print('开始构建前端')

subprocess.run(['pnpm', 'build'], shell=shell)

print('切换工作目录到client')

os.chdir('../client')
print(f'当前工作目录：{os.getcwd()}')

print('删除旧的前端文件')

shutil.rmtree('dist', ignore_errors=True)

# print('复制前端文件到客户端')

# shutil.copytree('../web/dist', 'dist', dirs_exist_ok=True)

# print('复制完成')

print('开始构建客户端')


bulid_commend = ['nuitka', '--onefile', 'app.py',
                 '--include-data-dir=../web/dist=dist', '--output-dir=nuitka_dist', '--remove-output', '--assume-yes-for-downloads']
if platform.system() == 'Darwin':
    bulid_commend.append('--macos-create-app-bundle')
subprocess.run(bulid_commend, shell=shell)
# subprocess.run(['nuitka', '--mode=standalone', 'app.py', '--include-data-dir=../web/dist=dist'], shell=True)


print('构建完成')
# print('删除前端文件')

# shutil.rmtree('dist', ignore_errors=True)