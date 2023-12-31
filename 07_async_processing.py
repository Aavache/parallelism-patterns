import asyncio
import concurrent.futures


def square(x):
    print(f"square: {x}")
    return x * x


async def async_square(x):
    loop = asyncio.get_event_loop()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        result = await loop.run_in_executor(executor, square, x)
        print(f"result: {result}")
    return result


async def main():
    data = [1, 2, 3, 4, 5]
    tasks = [async_square(x) for x in data]

    results = await asyncio.gather(*tasks)
    print(results)


if __name__ == "__main__":
    asyncio.run(main())
