import asyncio
import concurrent.futures

def square(x):
    return x * x

async def async_square(x):
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, square, x)
    return result

async def main():
    data = [1, 2, 3, 4, 5]
    tasks = [async_square(x) for x in data]

    results = await asyncio.gather(*tasks)
    print(results)

if __name__ == "__main__":
    asyncio.run(main())
