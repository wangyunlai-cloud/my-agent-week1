import asyncio

async def fetch(url: str,semaphore:asyncio.Semaphore) -> str:
    try:
        async with semaphore:
            await asyncio.sleep(1)
            return f"✅ {url}"
    except asyncio.TimeoutError:
        return f"❌ {url} 超时错误"
    except Exception as e:
        return f"❌ {url} 发生错误"

async def main():
    semaphore = asyncio.Semaphore(5)
    tasks = [fetch(f"https://api{i}.com",semaphore) for i in range(1,10)]
    results = await asyncio.gather(*tasks)
    print(results)

asyncio.run(main())