import numpy as np

M = np.array([[0, 2, 1, 1, 1, 1, 1, 2, 1, 3],
              [2, 0, 1, 1, 1, 0, 0, 1, 1, 2],
              [1, 1, 0, 1, 1, 0, 0, 0, 0, 1],
              [1, 1, 1, 0, 1, 0, 0, 0, 0, 1],
              [1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
              [1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
              [2, 1, 0, 0, 0, 1, 1, 0, 1, 2],
              [1, 1, 0, 0, 0, 0, 0, 1, 0, 1],
              [3, 2, 1, 1, 1, 1, 1, 2, 1, 0]])


def pmi(M, positive=True):
    """
    点互信息
    """
    col_totals = M.sum(axis=0)  # 按列求和
    row_totals = M.sum(axis=1)  # 按行求和
    total = col_totals.sum()  # 总频次
    expected = np.outer(row_totals, col_totals) / total  # 获得每个元素的分子
    M = M / expected
    # Silence distracting warnings about log(0):
    with np.errstate(divide='ignore'):  # 不显示log(0)的警告
        M = np.log(M)
    M[np.isinf(M)] = 0.0  # log(0) = 0
    if positive:
        M[M < 0] = 0.0
    return M


M_pmi = pmi(M)

np.set_printoptions(precision=2)
print(M_pmi)

U, s, Vh = np.linalg.svd(M_pmi)

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
# plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

words = ["我", "喜欢", "自然", "语言", "处理", "爱", "深度", "学习", "机器", "。"]

for i in range(len(words)):
    plt.text(U[i, 0], U[i, 1], words[i])  # U中的前两维赌赢二维空间的坐标

plt.xlim(-0.5, 0)
plt.ylim(-0.5, 0.6)
plt.savefig('svd.pdf')
plt.show()
