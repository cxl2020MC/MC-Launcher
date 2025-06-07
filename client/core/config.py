import pathlib
import aiofiles.os
from pydantic import BaseModel
import aiofiles

class Config(BaseModel):
    debug: bool = False
    dev:  bool = False

    
path = pathlib.Path("./config")

async def create_config():
        await aiofiles.os.makedirs(path, exist_ok=True)
        with path.joinpath("config.json").open("w") as f:
            config = Config()
            f.write(config.model_dump_json())

async def load_config() -> Config:
    if not path.joinpath("config.json").exists():
        print("创建配置文件")
        await create_config()
    
    with path.joinpath("config.json").open("r") as f:
        config = Config.model_validate_json(f.read())
        print(config)
        return config