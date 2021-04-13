"""

O(n²)
"""


def sort(array):
    for i in range(len(array) - 1):
        min_index = i

        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]

    return array


print(sort([3, 2, 11, -1, 0]))
