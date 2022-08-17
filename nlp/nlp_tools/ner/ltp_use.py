from ltp import LTP
import time

# ltp = LTP()  # 默认加载 Small 模型
# ltp = LTP(pretrained_model_name_or_path="LTP/small")
ltp = LTP(pretrained_model_name_or_path="LTP/base1")
# 另外也可以接受一些已注册可自动下载的模型名(https://huggingface.co/LTP):
# 使用字典结果
# output = ltp.pipeline(
#     ["他叫汤姆去拿外衣。"], tasks=["cws", "pos", "ner", "srl", "dep", "sdp"]
# )
# print(output.cws)
# print(output.pos)
# print(output.sdp)

# 传统算法，比较快，但是精度略低
# ltp = LTP("LTP/legacy")
ltp = LTP("LTP/base1")
start_time = time.time()
cws, pos, ner = ltp.pipeline(
    # ["e5fa5e8a5f1c0f2e3n153di6E1VT34u8VvmeQ-Sl 王江 代码整洁，算法基础好，工程能力强，架构意识努力中  男  25  本科  上海  3年经验  17811941572  wang0624@foxmail.com"], tasks=["cws", "pos", "ner"]
    ["百度在线网络技术（北京）有限公司"], tasks=["cws", "pos", "ner"]
).to_tuple()
end_time = time.time()
print(end_time-start_time)
print(cws, pos, ner)
# print(ner)