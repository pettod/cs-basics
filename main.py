import math
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
from time import time


SPACE = 0


def merge(left, right):
    array = []
    while len(left) + len(right):
        if len(left) == 0:
            array += list(right)
            break
        elif len(right) == 0:
            array += list(left)
            break
        elif left[0] < right[0]:
            array.append(left[0])
            left = np.delete(left, 0)
        else:
            array.append(right[0])
            right = np.delete(right, 0)
    return np.array(array)


def merge_sort(array):
    global SPACE
    if len(array) <= 1:
        return array
    middle = len(array) // 2
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])
    SPACE += len(array)
    array = merge(left, right)
    return array


def main():
    global SPACE
    number_of_elements = [5*i for i in range(1, 200)]
    times = []
    spaces = []
    for elements in tqdm(number_of_elements):
        SPACE = 0
        array = np.arange(elements)
        np.random.shuffle(array)
        start_time = time()
        array = merge_sort(array)
        times.append(time() - start_time)
        spaces.append(SPACE)
    print("  n   | logn |  space  |  time")
    print("------|------|---------|-------")
    for elements, time_, space in zip(number_of_elements, times, spaces):
        print("{:5} | {:4} | {:7} | {:7}".format(elements, round(math.log2(elements), 2), space, round(time_, 5)))

    plt.subplot(2,2,1)
    plt.plot(number_of_elements, times, label="Measurements")
    plt.title("Measurements O(nlogn)")
    plt.xlabel("Number of elements to sort")
    plt.ylabel("Sorting time (s)")
    plt.subplot(2,2,2)
    plt.plot(number_of_elements, number_of_elements, label="O(n)")
    plt.title("O(n)")
    plt.xlabel("Number of elements to sort")
    plt.subplot(2,2,3)
    plt.plot(number_of_elements, np.array(number_of_elements) * np.log2(np.array(number_of_elements)), label="O(nlogn)")
    plt.title("O(nlogn)")
    plt.xlabel("Number of elements to sort")
    plt.subplot(2,2,4)
    plt.plot(number_of_elements, np.array(number_of_elements) * np.array(number_of_elements), label="O(n^2)")
    plt.title("O(n^2)")
    plt.xlabel("Number of elements to sort")
    plt.tight_layout()
    plt.plto()


main()
