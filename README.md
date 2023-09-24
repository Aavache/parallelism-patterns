# Multi-Task Design Patterns

![Python Logo](https://www.python.org/static/community_logos/python-logo.png)

Welcome to the Python Multi Task Design Patterns repository! This comprehensive guide explores various multiprocessing/thread design patterns in Python, helping you harness the power of multi-core processors to build efficient and concurrent applications.

# Examples

* [Using multiprocess pool API](https://github.com/Aavache/parallelism-patterns/blob/main/00_multiprocess_pool.py)
* [Generic multiprocess pool](https://github.com/Aavache/parallelism-patterns/blob/main/01_worker_pool.py)
* [Shared data](https://github.com/Aavache/parallelism-patterns/blob/main/02_shared_data.py)
* [Pipeline](https://github.com/Aavache/parallelism-patterns/blob/main/03_pipeline.py)
* [Producer-consumer](https://github.com/Aavache/parallelism-patterns/blob/main/04_producer_consumer.py)
* [Master-worker](https://github.com/Aavache/parallelism-patterns/blob/main/05_master_worker.py)
* [Map-reduce](https://github.com/Aavache/parallelism-patterns/blob/main/06_map_reduce.py)
* [Concurrency with asyncio](https://github.com/Aavache/parallelism-patterns/blob/main/07_async_processing.py)

# General guideline

1. Create queues, locks and shared memory as needed. specially useful to initialize queues as input/output of processes.
2. Implement the actual task in a static function, for our example we use the square of a number. it's common practice to have a infinite loop that terminates when the queue is empty.
3. Create processes/threads and give as arguments the queues and so on from 1) and the function from 2).
4. Start processes.
5. If queues are used, put data in the input queue. you might want to also add a final `none` to let the target function know that is completed!.
6. Join the processes
7. Deque the queue or get output values.

The example in [here](https://github.com/Aavache/parallelism-patterns/blob/main/01_worker_pool.py) can be the foundation for most cases.

# Q&A

When should I use multi-threading or multi-processing?
* Depends on whether the task at hand is bounded by CPU or by I/O. if the task is heavy in terms of CPU operations, you should choose multi-processing approaches. if instead, you are I/O bounded, you are better off trying multi-threading with concurrency.

What is `async` function and `await` in `asyncio`?
* `asyncio` is a library for concurrency. the `async` keyword is used to define a coroutine function. A coroutine is a special type of function that can be paused and resumed during its execution. the primary advantage of using `async` is that it marks a function as non-blocking. this means that when a coroutine encounters an `await` statement, it yields control back to the event loop, allowing other coroutines or tasks to execute.
