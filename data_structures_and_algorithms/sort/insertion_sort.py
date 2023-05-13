from typing import List


# 插入排序
def insertion_sort(a: List[int]):
    length = len(a)
    if length <= 1:
        return
    # 取无序区第一个元素与有序区从后到前的元素一一进行比较，找到位置并插入（升序序列）
    for i in range(1, length):
        value = a[i]
        j = i - 1
        while j >= 0 and a[j] > value:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = value


if __name__ == "__main__":
    array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    insertion_sort(array)
    print(array)
