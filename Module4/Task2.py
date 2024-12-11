array = [1, 4, 2, 6, 3, 99, 64, 5, 7, 8]

def sort_insertion(array):
    for i in range(1, len(array)):
        for j in range(i):
            if array[i] > array[-len(array) + j]:
                continue
            else:
                array[i], array[-len(array) + j] = array[-len(array) + j], array[i]
    return array


print(sort_insertion(array))