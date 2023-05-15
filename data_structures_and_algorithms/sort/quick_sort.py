# from typing import List
# import random
#
#
# def quick_sort(a: List[int]):
#     _quick_sort_between(a, 0, len(a) - 1)
#
#
# def _quick_sort_between(a: List[int], low: int, high: int):
#     if low < high:
#         # get a random position as the pivot
#         k = random.randint(low, high)
#         a[low], a[k] = a[k], a[low]
#
#         m = _partition(a, low, high)  # a[m] is in final position
#         _quick_sort_between(a, low, m - 1)
#         _quick_sort_between(a, m + 1, high)
#
#
# def _partition(a: List[int], low: int, high: int):
#     pivot, j = a[low], low
#     for i in range(low + 1, high + 1):
#         if a[i] <= pivot:
#             j += 1
#             a[j], a[i] = a[i], a[j]  # swap
#     a[low], a[j] = a[j], a[low]
#     return j
#
#
# def test_quick_sort():
#     a1 = [3, 5, 6, 7, 8]
#     quick_sort(a1)
#     assert a1 == [3, 5, 6, 7, 8]
#     a2 = [2, 2, 2, 2]
#     quick_sort(a2)
#     assert a2 == [2, 2, 2, 2]
#     a3 = [4, 3, 2, 1]
#     quick_sort(a3)
#     assert a3 == [1, 2, 3, 4]
#     a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
#     quick_sort(a4)
#     assert a4 == [-2, -1, 3, 3, 5, 7, 8, 9, 9]
#
#
# if __name__ == "__main__":
#     a1 = [3, 5, 6, 7, 8]
#     a2 = [2, 2, 2, 2]
#     a3 = [4, 3, 2, 1]
#     a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
#     quick_sort(a1)
#     print(a1)
#     quick_sort(a2)
#     print(a2)
#     quick_sort(a3)
#     print(a3)
#     quick_sort(a4)
#     print(a4)


"""
方法一
"""


def quick_1(arr):
    if arr == []:
        return arr
    else:
        first = arr[0]
        less = quick_1([l for l in arr[1:0] if l < first])
        more = quick_1([m for m in arr[1:0] if m > first])
        return less + [first] + more


"""
方法二
"""


def quick_2(arr, i, j):
    if i >= j:
        return arr

    pivot = arr[i]  # 此时arr[i]将数值赋值给pivot，则自身相当于为空
    low = i
    high = j
    while i < j:
        while i < j and arr[j] >= pivot:  # 数组从后向前遍历当小于pivot时则将当前值赋值给arr[i]相当于为空的位置
            j -= 1
        arr[i] = arr[j]
        while i < j and arr[i] <= pivot:
            i += 1
        arr[j] = arr[i]
    arr[i] = pivot  # 此时i==j，pivot为数组元素的中间值
    quick_2(arr, low, i - 1)
    quick_2(arr, i + 1, high)
    return arr


if __name__ == "__main__":
    array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    # print(quick_1(array))
    print(quick_2(array, 0, len(array)-1))
