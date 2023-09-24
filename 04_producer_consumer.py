"""In producer-consumer pattern, the producer process generates data and puts it into a shared queue.

The consumer then takes data from the queue and processes it
"""
import multiprocessing
import time


def producer(queue):
    for i in range(5):
        time.sleep(1)  # Simulate some work
        item = f"Item {i}"
        queue.put(item)
        print(f"Produced: {item}")


def consumer(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        time.sleep(0.5)  # Simulate some work
        print(f"Consumed: {item}")


if __name__ == "__main__":
    queue = multiprocessing.Queue()  # Shared queue
    producer_process = multiprocessing.Process(target=producer, args=(queue,))
    consumer_process = multiprocessing.Process(target=consumer, args=(queue,))

    producer_process.start()
    consumer_process.start()

    producer_process.join()
    queue.put(None)  # Signal the consumer to stop
    consumer_process.join()
