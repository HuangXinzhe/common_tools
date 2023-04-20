# 安装简繁体转换工具
# pip install opencc

# 执行转换
# $ python 文件名.py input_file > output_file

import sys
import opencc

converter = opencc.OpenCC("t2s")
f_in = open(sys.argv[1], "r")

for line in f_in.readlines():
    line = line.strip()
    line_t2s = converter.convert(line)
    print(line_t2s)
