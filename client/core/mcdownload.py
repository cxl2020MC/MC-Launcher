import aiofiles
import aiohttp
import asyncio
import yarl

class MCDownload:
    def __init__(self, url: str = "https://bmclapi2.bangbang93.com", max_concurrent_tasks:  int = 128):
        self.url = url
        self.semaphore = asyncio.Semaphore(max_concurrent_tasks)
    
    async def get_version_list(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url) as response:
                return await response.json()
    async def download(self, path):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url) as response:
                if response.status == 200:
                    async with aiofiles.open(path, mode='wb') as f:
                        await f.write(await response.read())




