import aspose.words as aw
import re


def convert(file, suffix):
    """
    文件格式转换
    可以完成大多数格式之间的转换
    
    :param file: 想要转换的文件
    :param suffix: 想要转换成的文件格式
    :return: 返回原始文件名的新文件格式文件
    """
    # 输入想输入的任何格式的文本
    input_file = aw.Document(file)

    file_name = re.search('/?(.*?)\.', file).group(1)

    # 输出想要输出的格式文本，提供输出文件名及所要输入格式后缀
    output_file = input_file.save(file_name + '.' + suffix)

    return output_file

if __name__ == "__main__":
    convert('resume_paper.pdf', 'txt')