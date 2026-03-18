import asyncio
import random
from functools import wraps

def retry(max_retries = 5,base_delay = 1,max_delay = 16):

    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    retries += 1
                    delay = min(base_delay*(2**retries),max_delay)
                    print(f"任务失败,正在第{retries}次重试...,需要等待{delay}秒")
                    await asyncio.sleep(delay)
            raise Exception(f"任务重试{retries}后仍失败")
        return wrapper
    return decorator

@retry(max_retries = 5,base_delay = 1,max_delay = 16)
async def perfrom_task():
    if random.random()<0.9:
        raise ValueError("任务失败")
    return "任务成功"

async def main():
    try:
        result = await perfrom_task()
        print(result)
    except Exception as e:
        print(e)

asyncio.run(main())



