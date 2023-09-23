import multiprocessing


def square(x):
    return x * x


def map_function(data, result_queue):
    results = [square(x) for x in data]
    result_queue.put(results)


def reduce_function(result_queues):
    total = 0
    for result_queue in result_queues:
        results = result_queue.get()
        total += sum(results)
    return total


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    num_processes = 4

    # Split data into chunks
    chunk_size = len(data) // num_processes
    data_chunks = [data[i : i + chunk_size] for i in range(0, len(data), chunk_size)]

    # Create result queues
    result_queues = [multiprocessing.Queue() for _ in range(num_processes)]

    # Start map processes
    map_processes = []
    for i in range(num_processes):
        p = multiprocessing.Process(target=map_function, args=(data_chunks[i], result_queues[i]))
        map_processes.append(p)
        p.start()

    # Wait for map processes to finish
    for p in map_processes:
        p.join()

    # Start reduce process
    reduce_process = multiprocessing.Process(target=reduce_function, args=(result_queues,))
    reduce_process.start()
    reduce_process.join()

    total_sum = reduce_process.exitcode
    print("Total Sum of Squares:", total_sum)
