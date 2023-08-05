from pprint import pprint
import multiprocessing
import time



def factorize(num, results_queue):
    factors = set()
    for i in range(1, num+1):
        if num % i == 0:
            factors.add(i)
    pprint(factors)
    results_queue.put((num, factors))


def parallel_factorize(numbers):
    num_cores = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(num_cores)
    manager = multiprocessing.Manager()
    results_queue = manager.Queue()

    for num in numbers:
        pool.apply_async(factorize, args=(num, results_queue))
    
    pool.close()
    pool.join()

    results = {}

    while not results_queue.empty():
        num, factors = results_queue.get() 
        results[num] = factors
    return results


if __name__ == "__main__":
    start_time = time.time()
    results =  parallel_factorize([128, 255, 99999, 10651060])
    end_time = time.time()
    execution_time = end_time - start_time
    pprint(results)
    print(f"start {start_time} s\nExecution time: {execution_time} s\nend {end_time} s")



# assert a == [1, 2, 4, 8, 16, 32, 64, 128]
# assert b == [1, 3, 5, 15, 17, 51, 85, 255]
# assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
# assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]