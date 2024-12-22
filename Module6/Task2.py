from concurrent.futures import ProcessPoolExecutor
from time import time

def calcs1(_):
    print("Start calculating")
    a = 300 ** 3000000
    print("End")

# Sequential Execution
start = time()
calcs1(None)
calcs1(None)
sequential_time = time() - start
print(f"Sequential execution time: {sequential_time:.2f} seconds")

# Parallel Execution
start = time()
with ProcessPoolExecutor(max_workers=1) as executor:
    executor.map(calcs1, range(2))
print(time() - start)