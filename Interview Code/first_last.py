# @author   Lucas Cardoso de Medeiros
# @since    06/06/2022
# @version  1.0

# FIRST & LAST

# Rules:
# Given the sorted arr array of integers and integer target
# Find the index of the first and last position of the first and last position of target in arr
# If it can't be found return [-1,-1]

# Example:
# arr = [2, 4, 5, 5, 5, 5, 5, 7, 9, 9]
# target = 5

# Solution 1: brute force
# O(n) complexity
def first_last(arr, target):
    for num in arr:
        if num == target:
            first = arr.index(num)
            i = first
            while arr[i] == target:
                if arr[i + 1] != target:
                    last = i
                    return [first, last]
                i += 1
    return [-1, -1]


# Solution 2: binary search (x2)
# T(n) = 2 * O(logn) = O(logn) complexity
def find_first(arr, target):
    if arr[0] == target:
        return 0
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target and arr[mid - 1] < target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def find_last(arr, target):
    if arr[-1] == target:
        return len(arr) - 1
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target and arr[mid + 1] > target:
            return mid
        elif arr[mid] > target:
            right = mid + 1
        else:
            left = mid - 1
    return -1


def first_last_binary(arr, target):
    if len(arr) == 0 or arr[0] > target or arr[-1] < target:
        return [-1, -1]
    return [find_first(arr, target), find_last(arr, target)]


if __name__ == '__main__':
    arr = [2, 4, 5, 5, 5, 5, 5, 7, 9, 9]
    target = 5

    print(first_last_binary(arr, target))
