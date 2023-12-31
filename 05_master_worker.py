"""In this example, we will use a master-worker pattern to distribute tasks to multiple processes.
The master process will create a task queue and a result queue. It will then create a number of worker processes and
distribute tasks to them.
"""
import multiprocessing


def worker(task_queue, result_queue):
    while True:
        task = task_queue.get()
        if task is None:
            break
        result = task**2  # Example task processing
        result_queue.put(result)


def master():
    num_workers = 4
    task_queue = multiprocessing.Queue()
    result_queue = multiprocessing.Queue()

    # Start worker processes
    workers = [multiprocessing.Process(target=worker, args=(task_queue, result_queue)) for _ in range(num_workers)]
    for w in workers:
        w.start()

    # Add tasks to the queue
    tasks = [1, 2, 3, 4, 5]
    for task in tasks:
        task_queue.put(task)

    # Add termination signal to the queue
    for _ in range(num_workers):
        task_queue.put(None)

    # Wait for workers to finish
    for w in workers:
        w.join()

    # Collect results
    results = []
    while not result_queue.empty():
        results.append(result_queue.get())

    print(results)


if __name__ == "__main__":
    master()
