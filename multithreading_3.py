import threading
import time
from concurrent.futures import ThreadPoolExecutor

# Indicates some task being done
def func(seconds):

    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    return seconds

def main():

    time1 = time.perf_counter()

    # Normal Code
    # func(4)
    # func(3)
    # func(2)
    # func(1)

    # time2 = time.perf_counter()
    # print(time2 - time1)

    # Same Code using threads
    t1 = threading.Thread(target=func, args=[4])
    t2 = threading.Thread(target=func, args=[3])
    t3 = threading.Thread(target=func, args=[2])
    t4 = threading.Thread(target=func, args=[1])

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

    # Calculating Time
    time2 = time.perf_counter()
    print(time2 - time1)

def poolingDemo():

    with ThreadPoolExecutor() as executor:

        l = [5,6,7,8]
        results = executor.map(func,l)

        for result in results:
            print(result)     

poolingDemo()

