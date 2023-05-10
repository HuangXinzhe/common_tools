"""
    实现标记和索引之间的相互映射
"""

from collections import defaultdict, Counter


class Vocab:
    def __init__(self, tokens=None):
        self.idx_to_token = list()
        self.token_to_idx = dict()

        if tokens is not None:
            if "<unk>" not in tokens:
                tokens = tokens + ["<unk>"]
            for token in tokens:
                self.idx_to_token.append(token)
                self.token_to_idx[token] = len(self.idx_to_token) - 1
            self.unk = self.token_to_idx['<unk>']

    @classmethod  # 类方法，在完成标记与映射之前完成对文本中所有标记的统计
    def build(cls, text, min_freq=1, reserved_tokens=None):
        token_freqs = defaultdict(int)  # 创建一个字典，字典中的值为int类型，且无论是否存在键都会有个默认值
        for sentence in text:
            for token in sentence:
                token_freqs[token] += 1
        uniq_tokens = ["<unk>"] + (reserved_tokens if reserved_tokens else [])  # reserved_tokens表示预留的一些token
        uniq_tokens += [token for token, freq in token_freqs.items() \
                        if freq >= min_freq and token != "<unk>"]  # 记录文本中所有的token
        return cls(uniq_tokens)

    def __len__(self):
        # 词表大小
        return len(self.idx_to_token)

    def __getitem__(self, token):
        # 查找输入标记的索引值，如果该标记不存在则返回<unk>的索引值
        return self.token_to_idx.get(token, self.unk)

    def convert_tokens_to_ids(self, tokens):
        # 查找一系列输入标记对应的索引值
        return [self[token] for token in tokens]

    def convert_ids_to_tokens(self, indices):
        # 查找一系列索引值对应的标记
        return [self.idx_to_token[index] for index in indices]


def save_vocab(vocab, path):
    with open(path, 'w') as writer:
        writer.write("\n".join(vocab.idx_to_token))


def read_vocab(path):
    with open(path, 'r') as f:
        tokens = f.read().split('\n')
    return Vocab(tokens)
