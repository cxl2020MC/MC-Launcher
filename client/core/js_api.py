import asyncio
import threading


async def async_test():
    print("test")
    return "test"

class Api:
    def __init__(self):
        self.loop = asyncio.new_event_loop()

    # 包装异步函数为同步方法
    def run_async(self, async_func):
        return asyncio.run_coroutine_threadsafe(async_func, self.loop).result()

    # 启动事件循环的线程
    def start_loop(self):
        threading.Thread(target=self._run_loop, daemon=True).start()

    def _run_loop(self):
        asyncio.set_event_loop(self.loop)
        self.loop.run_forever()

    def test_async(self):
        return self.run_async(async_test())
    