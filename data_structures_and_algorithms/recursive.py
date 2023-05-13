"""
递归算法
走楼梯，每次只能走一阶或二阶，给定楼梯的阶数，得到可能的走法
"""
import time

# 递归的方式完成
def recursive(n):
    if n <= 2:
        return n
    else:
        return recursive(n - 1) + recursive(n - 2)


# 非递归的方式完成
def non_recursive(n):
    if n <= 2:
        return n
    else:
        n_1 = 1
        n_2 = 2
        count = 1
        while count < n - 1:
            n_1, n_2 = n_2, n_1 + n_2
            count += 1
        return n_2


if __name__ == "__main__":
    n = int(input(f"Please input your number:"))

    start_time_1 = time.time()
    print(recursive(n))
    end_time_1 = time.time()
    print(f'recursive:{start_time_1-end_time_1}')

    start_time_2 = time.time()
    print(non_recursive(n))
    end_time_2 = time.time()
    print(f'non_recursive:{start_time_2-end_time_2}')

