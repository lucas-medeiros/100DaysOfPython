# @author   Lucas Cardoso de Medeiros
# @since    06/06/2022
# @version  1.0

# Kth LARGEST ELEMENT

# Rules:
# Given the array of integers arr and integer k
# Find the kth largest element
# If it can't be found return [-1,-1]

# Example:
# arr = [4, 2, 9, 7, 5, 6, 7, 1, 3]
# k = 4
# output = 6

# Explanation
# 1st largest element: 9
# 2nd largest element: 7
# 3rd largest element: 7
# 4th largest element: 6

import heapq


# Solution 1: sort
# O(nlogn) complexity
def kth_largest_sort(arr, k):
    if len(arr) == 0:
        return -1
    sorted_arr = sorted(arr, reverse=True)
    return sorted_arr[k - 1]


# Solution 2: heap
# O(n + klogn) complexity
def kth_largest_heap(arr, k):
    if len(arr) == 0:
        return -1
    arr = [-elem for elem in arr]
    heapq.heapify(arr)
    for i in range(k - 1):
        heapq.heappop(arr)
    return -heapq.heappop(arr)


if __name__ == '__main__':
    arr = [4, 2, 9, 7, 5, 6, 7, 1, 3]
    k = 4

    print(kth_largest_sort(arr, k))
    print(kth_largest_heap(arr, k))
