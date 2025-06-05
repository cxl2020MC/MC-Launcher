import pathlib
# import aiofiles

path = pathlib.Path("./config")

if not path.exists():
    print("创建配置文件目录")
    path.mkdir()

# with path.joinpath("config.json").open("w") as f:
    # f.write("{}")