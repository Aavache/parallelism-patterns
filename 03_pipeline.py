import multiprocessing


def stage1(input_data, output_queue):
    for item in input_data:
        processed_item = item * 2
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

    stage1_output_queue = multiprocessing.Queue()
    stage2_output_queue = multiprocessing.Queue()

    stage1_process = multiprocessing.Process(target=stage1, args=(input_data, stage1_output_queue))
    stage2_process = multiprocessing.Process(target=stage2, args=(stage1_output_queue, stage2_output_queue))

    stage1_process.start()
    stage2_process.start()

    stage1_process.join()
    stage1_output_queue.put(None)  # Signal the next stage to stop
    stage2_process.join()

    results = []
    while not stage2_output_queue.empty():
        results.append(stage2_output_queue.get())

    print(results)
