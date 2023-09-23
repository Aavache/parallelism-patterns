import multiprocessing


def increment_shared_counter(counter, lock):
    for _ in range(100000):
        with lock:
            counter.value += 1


if __name__ == "__main__":
    counter = multiprocessing.Value("i", 0)
    lock = multiprocessing.Lock()
    processes = [multiprocessing.Process(target=increment_shared_counter, args=(counter, lock)) for _ in range(4)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print("Final Counter Value:", counter.value)
