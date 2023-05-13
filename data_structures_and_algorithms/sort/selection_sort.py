from typing import List


# 选择排序
def selection_sort(a: List[int]):
    length = len(a)
    if length <= 1:
        return

    for i in range(length):
        min_index = i
        min_val = a[i]
        for j in range(i, length):
            if a[j] < min_val:
                min_val = a[j]
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]


if __name__ == "__main__":
    array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    selection_sort(array)
    print(array)
