import aiofiles
import aiohttp
import asyncio

class MCDownload:
    def __init__(self, url, max_concurrent_tasks:  int = 128):
        self.url = url
        self.semaphore = asyncio.Semaphore(max_concurrent_tasks)
    
    async def download(self, path):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url) as response:
                if response.status == 200:
                    async with aiofiles.open(path, mode='wb') as f:
                        await f.write(await response.read())




