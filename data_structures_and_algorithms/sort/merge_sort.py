# from typing import List
#
#
# def merge_sort(a: List[int]):
#     _merge_sort_between(a, 0, len(a) - 1)
#
#
# def _merge_sort_between(a: List[int], low: int, high: int):
#     # The indices are inclusive for both low and high.
#     if low < high:
#         mid = low + (high - low) // 2
#         _merge_sort_between(a, low, mid)
#         _merge_sort_between(a, mid + 1, high)
#         _merge(a, low, mid, high)
#
#
# def _merge(a: List[int], low: int, mid: int, high: int):
#     # a[low:mid], a[mid+1, high] are sorted.
#     i, j = low, mid + 1
#     tmp = []
#     while i <= mid and j <= high:
#         if a[i] <= a[j]:
#             tmp.append(a[i])
#             i += 1
#         else:
#             tmp.append(a[j])
#             j += 1
#     start = i if i <= mid else j
#     end = mid if i <= mid else high
#     tmp.extend(a[start:end + 1])
#     a[low:high + 1] = tmp
#
#
# def test_merge_sort():
#     a1 = [3, 5, 6, 7, 8]
#     merge_sort(a1)
#     assert a1 == [3, 5, 6, 7, 8]
#     a2 = [2, 2, 2, 2]
#     merge_sort(a2)
#     assert a2 == [2, 2, 2, 2]
#     a3 = [4, 3, 2, 1]
#     merge_sort(a3)
#     assert a3 == [1, 2, 3, 4]
#     a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
#     merge_sort(a4)
#     assert a4 == [-2, -1, 3, 3, 5, 7, 8, 9, 9]
#
#
# if __name__ == "__main__":
#     a1 = [3, 5, 6, 7, 8]
#     a2 = [2, 2, 2, 2]
#     a3 = [4, 3, 2, 1]
#     a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
#     merge_sort(a1)
#     print(a1)
#     merge_sort(a2)
#     print(a2)
#     merge_sort(a3)
#     print(a3)
#     merge_sort(a4)
#     print(a4)

import math


def merge_sort(arr):
    if len(arr) < 2:
        return arr

    middle = math.floor(len(arr) / 2)
    left, right = arr[:middle], arr[middle:]
    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))  # pop()函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))

    while right:
        result.append(right.pop(0))

    return result


if __name__ == "__main__":
    array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    print(merge_sort(array))
