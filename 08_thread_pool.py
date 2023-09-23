import concurrent.futures


def square(x):
    return x * x


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(square, data))

    print(results)
