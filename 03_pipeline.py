"""Pipeline example using multiprocessing.

it shows how to use multiprocessing to create a pipeline of processes that pass data between each other using Queues
"""
import multiprocessing


def stage1(in_queue, output_queue):
    while True:
        item = in_queue.get()
        if item is None:
            break
        processed_item = item**2
        output_queue.put(processed_item)


def stage2(input_queue, output_queue):
    while True:
        item = input_queue.get()
        if item is None:
            break
        processed_item = item + 10
        output_queue.put(processed_item)


if __name__ == "__main__":
    input_data = [1, 2, 3, 4, 5]

    stage1_in_queue = multiprocessing.Queue()
    stage1_out_queue = multiprocessing.Queue()
    stage2_out_queue = multiprocessing.Queue()

    stage1_process = multiprocessing.Process(target=stage1, args=(stage1_in_queue, stage1_out_queue))
    stage2_process = multiprocessing.Process(target=stage2, args=(stage1_out_queue, stage2_out_queue))

    stage1_process.start()
    stage2_process.start()

    for item in input_data:
        stage1_in_queue.put(item)

    stage1_process.join()
    stage1_out_queue.put(None)  # Signal the next stage to stop
    stage2_process.join()

    results = []
    while not stage2_out_queue.empty():
        results.append(stage2_out_queue.get())

    print(results)
