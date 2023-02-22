from transformers import BertConfig, BertModel

# ================================第一部分===============================
# Building the config
# config = BertConfig()  # 配置包含各种属性

# Building the model from the config
# model = BertModel(config)  # 通过属性构建模型

# print(config)

# Model is randomly initialized!
# 此时模型是随机初始化的

# ================================第二部分===============================
model = BertModel.from_pretrained("bert-base-cased")

# 保存模型
# config.json，构建模型体系结构所需的属性，checkpoint来源
# pytorch_model.bin，state dictionary，包含模型所有的权重
model.save_pretrained("directory_on_my_computer")