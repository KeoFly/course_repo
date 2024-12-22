import time
from threading import Thread
from multiprocessing.pool import ThreadPool
from multiprocessing import Pool

"""
def start_rocket(number):
    time.sleep(3)
    print(f"Rocket № {number} started!")

threads = [Thread(target=start_rocket, args=(i + 1, )) for i in range(5)]

for t in threads:
    t.start()

for t in threads:
    t.join()"""

"""def thread_func():
    print("Стартуем поток")
    time.sleep(2)
    print("Завершаем поток")
print("Запускаем программу")
t = Thread(target=thread_func(), daemon=True)
t.start()
print("Завершаем программу")"""


"""def thread_func2(name):
    print(f"Стартуем поток {name}")
    time.sleep(2)
    print(f"Завершаем поток {name}")

with ThreadPool(processes=7) as executor:
    executor.map(thread_func2, range(15))"""

"""def thread_func3(name):
    print(f"Стартуем поток {name}")
    time.sleep(2)
    print(f"Завершаем поток {name}")

if __name__ == "__main__":
    with Pool(processes=7) as executor:
        executor.map(thread_func3, range(15))"""

"""def thread_func4(name):
    print(f"Стартуем поток {name}")
    a = 300**3000000
    print(f"Завершаем поток {name}")

if __name__ == "__main__":
    start_time = time.time()
    with Pool(processes=3) as executor:
        executor.map(thread_func4, range(3))
    duration = time.time() - start_time
    print(duration)"""


