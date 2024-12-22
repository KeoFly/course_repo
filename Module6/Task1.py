import time
from multiprocessing.pool import ThreadPool

def get_thread(thread_name):
    time.sleep(1)
    print(thread_name)


with ThreadPool(processes=5) as executor:
    executor.map(get_thread, range(5))