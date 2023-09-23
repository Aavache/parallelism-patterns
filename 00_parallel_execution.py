import multiprocessing


def square(x):
    return x * x


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    pool = multiprocessing.Pool(processes=4)  # Use 4 processes
    results = pool.map(square, data)
    pool.close()
    pool.join()
    print(results)
