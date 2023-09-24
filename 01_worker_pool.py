"""Example of a worker pool using multiprocessing.

It is common convention to use two queues, one for input and one for output. This way, the worker processes can be
independent of each other and the main process can collect the results when they are ready.
"""
import multiprocessing


def worker(in_queue, out_queue):
    """Independent worker process that processes tasks from a queue and puts results in another queue."""
    while True:
        task = in_queue.get()
        if task is None:
            break
        result = task**2  # Example task processing, square the number
        out_queue.put(result)


if __name__ == "__main__":
    num_workers = 4
    in_queue = multiprocessing.Queue()
    out_queue = multiprocessing.Queue()

    # 1. Start worker processes
    workers = [multiprocessing.Process(target=worker, args=(in_queue, out_queue)) for _ in range(num_workers)]
    for w in workers:
        w.start()

    # 2. Add tasks to the queue
    tasks = [1, 2, 3, 4, 5]
    for task in tasks:
        in_queue.put(task)

    # 3. Add termination signal to the input queue
    for _ in range(num_workers):
        in_queue.put(None)

    # 4. Wait for workers to finish
    for w in workers:
        w.join()

    # 5. Collect results
    results = []
    while not out_queue.empty():
        results.append(out_queue.get())

    print(results)
