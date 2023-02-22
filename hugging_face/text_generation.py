from transformers import pipeline

"""
主要使用方法是您提供一个提示，模型将通过生成剩余的文本来自动完成整段话。
文本生成涉及随机性，如果每次可能都会得到不相同的结果。
"""

# generator = pipeline("text-generation")
# answer = generator("In this course, we will teach you how to",
#                    num_return_sequences=2,
#                    max_length=15)  # 生成2个句子，每个句子最大长队15
# print(answer)


generator = pipeline("text-generation", model="distilgpt2")
answer = generator(
    "In this course, we will teach you how to",
    max_length=30,
    num_return_sequences=2,
)
print(answer)
