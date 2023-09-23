import multiprocessing

def square(x):
    return x * x

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]

    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(square, data)

    print(results)
