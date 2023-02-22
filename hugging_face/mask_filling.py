from transformers import pipeline

"""
top_k 参数控制要显示的结果有多少种。
请注意，这里模型填充了特殊的<mask>词，被称为掩码标记。
其他掩码填充模型可能有不同的掩码标记，在探索其他模型时要验证正确的掩码字是什么。
"""

unmasker = pipeline("fill-mask")
answer = unmasker(
    "This course will teach you all about <mask> models.",
    top_k=2
)
print(answer)