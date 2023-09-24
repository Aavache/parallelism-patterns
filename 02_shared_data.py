"""Sharing data between processes using Value and lock."""
import multiprocessing


def increment_shared_counter(counter, lock):
    """Increment a shared counter 100000 times."""
    for _ in range(100000):
        with lock:
            # The lock ensures that only one process
            # can access the counter at a time
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
